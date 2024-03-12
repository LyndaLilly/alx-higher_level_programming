#!/usr/bin/node
exports.esrever = function (list) {
  let wt = list.length - 1;
  let m = 0;
  while ((wt - m) > 0) {
    const aux = list[wt];
    list[wt] = list[m];
    list[m] = aux;
    m++;
    wt--;
  }
  return list;
};
