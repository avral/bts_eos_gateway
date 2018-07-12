# TODO Сентри

# FIXME
# GATEWAY_ACCOUNT = os.getenv('GATEWAY_ACCOUNT')
NODE_URL = os.getenv('BITSHARES_NODE_URL', 'wss://node.testnet.bitshares.eu')
GATEWAY_ACCOUNT_ID = os.getenv('GATEWAY_ACCOUNT', '1.2.3604')
GATEWAY_ACCOUNT_WIF = '5KiQYz2MBTWH676biQcVwx6zJ1J3cYb65bZThRBav1z7gU2MoMu'

bitshares = BitShares(node=NODE_URL, keys=[GATEWAY_ACCOUNT_WIF])
set_shared_blockchain_instance(bitshares)

m = Memo()


logger.info(f'Gateway running..')
logger.info(f'NODE_URL: {NODE_URL}')
logger.info(f'GATEWAY_ACCOUNT_ID: {GATEWAY_ACCOUNT_ID}')
logger.info(f'GATEWAY_ACCOUNT_WIF: {GATEWAY_ACCOUNT_WIF[:5]}..')
logger.info(f'EOS_NODE_URL: {eosio_config.url}')
logger.info(f'EOS_NODE_PORT: {eosio_config.port}')
logger.info(f'ISSUER_WIF: {ISSUER_WIF}')
logger.info(f'ISSUER_NAME: {ISSUER_NAME}')
logger.info(f'ISSUE_ASSET: {ISSUE_ASSET}')


for op in Blockchain().stream(['transfer']):
    amount = float(op['amount']['amount']) / 100000

    if op['to'] != GATEWAY_ACCOUNT_ID:
        continue

    if 'memo' not in op:
        logger.warn(f'No memo: {op["from"]} | {amount} | {op["block_num"]}')
        continue

    try:
        # TODO Валидация есть ли такой eos юзер
        eos_receiver = m.decrypt(op['memo'])
    except Exception as e:
        logger.exception(f'Invalid memo {op["from"]} | {amount} | {op["block_num"]}')
        raise e

    # TODO Обработка исключений
    eos_issue(eos_receiver, amount)
