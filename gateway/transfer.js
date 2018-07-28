let Eos = require('tcjs');
let fs = require('fs');

let httpEndpoint = 'https://eost.travelchain.io';
let chainId = '45a05637a49d4d0a304f5d8f553eb7792cad6525d8664de30f0234c630520c60';

let from = process.argv[2];
let to = process.argv[3];
let amount = process.argv[4];

let keyProvider = [process.env.ISSUER_WIF];

eos = Eos({httpEndpoint, chainId, keyProvider, logger: {error: null}});

eos.transfer(from, to, amount, '')
  .then((data) => {
    console.log(JSON.stringify(data));
}).catch((e) => {
    // error in JSON
    console.log(e);
  });

