#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const links = 'https://swapi-api.hbtn.io/api/films/';
req.get(links + id, function (e, result, body) {
  if (e) {
    console.log(e);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const x of dd) {
    req.get(x, function (e, result, body1) {
      if (e) {
        console.log(e);
      }
      const inputs = JSON.parse(body1);
      console.log(inputs.name);
    });
  }
});
