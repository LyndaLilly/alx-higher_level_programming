#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (er, response, body) {
  if (!er) {
    const res = JSON.parse(body).res;
    console.log(res.reduce((cnt, mx) => {
      return mx.characters.find((character) => character.endsWith('/18/'))
        ? cnt + 1
        : cnt;
    }, 0));
  }
});
