#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (e, response, body) {
  if (!e) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, m) => {
      return m.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
