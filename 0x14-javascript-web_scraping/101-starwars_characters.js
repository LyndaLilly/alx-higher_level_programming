#!/usr/bin/node
const request = require('request');
const links = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(links, function (e, ansx, body) {
  if (!e) {
    const txts = JSON.parse(body).txts;
    printCharacters(txts, 0);
  }
});

function printCharacters (txts, nums) {
  request(txts[nums], function (e, ansx, body) {
    if (!e) {
      console.log(JSON.parse(body).name);
      if (nums + 1 < txts.length) {
        printCharacters(txts, nums + 1);
      }
    }
  });
}
