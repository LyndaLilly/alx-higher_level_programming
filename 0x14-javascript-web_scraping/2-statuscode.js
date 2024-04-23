#!/usr/bin/node

const request = require('request');
const links = process.argv[2];

request(links, function (e, response) {
  if (e) {
    console.log(e);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
