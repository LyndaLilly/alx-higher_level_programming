#!/usr/bin/node
const fs = require('fs');

const prep = fs.readFileSync(process.argv[2]).toString();
const rupes = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], prep + rupes);
