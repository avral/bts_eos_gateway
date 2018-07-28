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

## .env file:

KEY: DEFAULT_VALUE

```
EOS_NODE_URL=https://eost.travelchain.io
EOS_NODE_PORT=443

ISSUER_WIF=
ISSUER_NAME=
ISSUE_ASSET=

BITSHARES_NODE_URL=wss://node.testnet.bitshares.eu
GATEWAY_ACCOUNT=
GATEWAY_ACCOUNT_WIF=

DEBUG="false"
START_BLOCK: <default: current block>
```
