import os
import logging
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.core.cache import cache
from bitshares import BitShares
from bitshares.blockchain import Blockchain
from bitshares.memo import Memo
from bitshares.instance import set_shared_blockchain_instance
from raven.contrib.django.raven_compat.models import client

from gateway.utils import account_exists
from gateway.models import Transfer

from gateway.eos import (
    eos_issue, eosio_config, ISSUE_ASSET, ISSUER_NAME, ISSUER_WIF
)

logging.basicConfig(
    level=logging.WARN,
    format="%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s",
    handlers=[
        # logging.FileHandler("{0}/{1}.log".format(logPath, fileName)),
        logging.StreamHandler()
    ])

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

NODE_URL = os.getenv('BITSHARES_NODE_URL', 'wss://node.testnet.bitshares.eu')
GATEWAY_ACCOUNT_ID = os.getenv('GATEWAY_ACCOUNT', '1.2.3604')
GATEWAY_ACCOUNT_WIF = '5KiQYz2MBTWH676biQcVwx6zJ1J3cYb65bZThRBav1z7gU2MoMu'
START_BLOCK = os.getenv('START_BLOCK', cache.get('START_BLOCK'))

if START_BLOCK:
    START_BLOCK = int(START_BLOCK)

bitshares = BitShares(node=NODE_URL, keys=[GATEWAY_ACCOUNT_WIF])
set_shared_blockchain_instance(bitshares)

m = Memo()


logger.info('Gateway running..')
logger.info(f'START_BLOCK: {START_BLOCK}')
logger.info(f'NODE_URL: {NODE_URL}')
logger.info(f'GATEWAY_ACCOUNT_ID: {GATEWAY_ACCOUNT_ID}')
logger.info(f'GATEWAY_ACCOUNT_WIF: {GATEWAY_ACCOUNT_WIF[:5]}..')
logger.info(f'EOS_NODE_URL: {eosio_config.url}')
logger.info(f'EOS_NODE_PORT: {eosio_config.port}')
logger.info(f'ISSUER_WIF: {ISSUER_WIF}')
logger.info(f'ISSUER_NAME: {ISSUER_NAME}')
logger.info(f'ISSUE_ASSET: {ISSUE_ASSET}')


def parse_transfer(op):
    # TODO Разобраться где обрабатывать пресижн
    amount = Decimal(op['amount']['amount']) / 100000
    bts_name = bitshares.rpc.get_account(op['from'])['name']

    transfer = Transfer.objects.create(
        amount=amount,
        bts_name=bts_name,
        block_num=op['block_num']
    )

    try:
        memo = m.decrypt(op.get('memo'))
    except ValueError:
        transfer.sys_message = 'Invalid memo: %s' % op.get('memo')
        transfer.is_valid_memo = False

    if not account_exists(memo):
        transfer.sys_message = f'Account does not exist: {memo}'
        transfer.is_valid_memo = False
    else:
        transfer.eos_name = memo

    return transfer


class Command(BaseCommand):
    def handle(self, *args, **options):
        for op in Blockchain().stream(['transfer'], start=START_BLOCK):
            block_num = op['block_num']
            cache.set('START_BLOCK', block_num + 1)

            if op['to'] != GATEWAY_ACCOUNT_ID:
                continue

            transfer = parse_transfer(op)

            if transfer.is_valid_memo:
                try:
                    eos_issue(transfer)
                except Exception:
                    logger.exception('Error emit tokens')
                    client.captureException()

            transfer.save()
