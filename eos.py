import os
import logging

from eosiopy import eosio_config
from eosiopy.eosioparams import EosioParams
from eosiopy.nodenetwork import NodeNetwork
from eosiopy.rawinputparams import RawinputParams


ISSUER_WIF = os.getenv('ISSUER_WIF', '5KPk8R4KMNzLQr3rxKqRYRnG5RB7d9X7o5sPc1r8mTuo5uTPwcn')
ISSUER_NAME = os.getenv('ISSUER_NAME', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')
ISSUE_ASSET = os.getenv('ISSUE_ASSET', 'TT')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


eosio_config.url = os.getenv('EOS_NODE_URL', 'https://eost.travelchain.io')
eosio_config.port = os.getenv('EOS_NODE_PORT', '443')


def eos_issue(receiver, amount, memo=''):
    quantity = f'{amount:.4f} {ISSUE_ASSET}'

    raw = RawinputParams('transfer', {
            'from': ISSUER_NAME,
            'memo': memo,
            'quantity': quantity,
            'to': receiver
        }, 'eosio.token', f'{ISSUER_NAME}@active')

    eosiop_arams = EosioParams(raw.params_actions_list, ISSUER_WIF)
    r = NodeNetwork.push_transaction(eosiop_arams.trx_json)

    if 'transaction_id' not in r:
        logging.error(f'Issuing eos tokens \n {r}')
    else:
        logger.info(f'Issued {quantity} for {receiver} -> {r["transaction_id"]}')
