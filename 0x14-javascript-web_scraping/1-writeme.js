#!/usr/bin/node
var abx = require('abx');
abx.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
