# bts_eos_gateway


## Run gateway
migrate database
```
docker-compose run --rm base python manage.py migrate
docker-compose run --rm base python manage.py createcachetable
```

create superuser for admin panel
`docker-compose run --rm base python manage.py createsuperuser`

## build docker image
`docker-compose build`

run gateway `docker-compose up`

## environments:

KEY: DEFAULT_VALUE

```
# eos
EOS_NODE_URL: https://eost.travelchain.io
EOS_NODE_PORT: 443

ISSUER_WIF: 
ISSUER_NAME: 
ISSUE_ASSET: TT

# BitShares
BITSHARES_NODE_URL: wss://node.testnet.bitshares.eu
GATEWAY_ACCOUNT: 1.2.3604 # Must be as ID
GATEWAY_ACCOUNT_WIF: ..
START_BLOCK: <default: current block>
```
