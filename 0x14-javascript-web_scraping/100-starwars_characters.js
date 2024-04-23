#!/usr/bin/node

const r = require('request');
const infos = process.argv[2];
const links = 'https://swapi-api.hbtn.io/api/films/';
r.get(links + infos, function (e, result, body) {
  if (e) {
    console.log(e);
  }
  const forms = JSON.parse(body);
  const fm = forms.characters;
  for (const x of fm) {
    r.get(x, function (e, result, body1) {
      if (e) {
        console.log(e);
      }
      const inputs = JSON.parse(body1);
      console.log(inputs.name);
    });
  }
});
