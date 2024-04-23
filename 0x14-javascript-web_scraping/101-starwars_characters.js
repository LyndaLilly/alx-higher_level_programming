#!/usr/bin/node
const request = require('request');
const links = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(links, function (e, response, body) {
  if (!e) {
    const txts = JSON.parse(body).txts;
    printCharacters(txts, 0);
  }
});

function printCharacters (txts, index) {
  request(txts[index], function (e, response, body) {
    if (!e) {
      console.log(JSON.parse(body).name);
      if (index + 1 < txts.length) {
        printCharacters(txts, index + 1);
      }
    }
  });
}
