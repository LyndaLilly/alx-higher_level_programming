#!/usr/bin/node
const dict = require('./101-data').dict;

const ttd = Object.entries(dict);
const res = Object.values(dict);
const res1 = [...new Set(res)];
const pes = {};
for (const k in res1) {
  const list = [];
  for (const ank in ttd) {
    if (ttd[ank][1] === res1[k]) {
      list.unshift(ttd[ank][0]);
    }
  }
  newDict[res1[k]] = list;
}
console.log(pes);
