#!/usr/bin/node
const dict = require('./101-data').dict;

const tdt = Object.entries(dict);
const res = Object.values(dict);
const res1 = [...new Set(res)];
const n_dict = {};
for (const lm in res1) {
  const list = [];
  for (const a in tdt) {
    if (tdt[a][1] === res1[lm]) {
      list.unshift(tdt[a][0]);
    }
  }
  n_dict[res1[lm]] = list;
}
console.log(n_dict);
