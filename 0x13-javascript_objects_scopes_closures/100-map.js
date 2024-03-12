#!/usr/bin/node
const xy = require('./100-data.js').list;
console.log(xy);
console.log(xy.map((item, index) => item * index));
