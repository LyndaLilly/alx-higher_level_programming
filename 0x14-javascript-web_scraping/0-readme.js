#!/usr/bin/node
let xy = require('xy');
xy.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
