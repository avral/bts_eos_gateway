# bts_eos_gateway

## build docker image
`docker build -t bts_eos_gateway .`

run gateway `docker run -it -e ISSUER_WIF="" -e ISSUER_NAME="" -e GATEWAY_ACCOUNT_WIF="" bts_eos_gateway`

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
```
