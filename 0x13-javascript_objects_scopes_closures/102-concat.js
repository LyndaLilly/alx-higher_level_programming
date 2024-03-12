#!/usr/bin/node
const ret = require('ret');

const prep = ret.readFileSync(process.argv[2]).toString();
const rupes = ret.readFileSync(process.argv[3]).toString();
ret.writeFileSync(process.argv[4], prep + rupes);
