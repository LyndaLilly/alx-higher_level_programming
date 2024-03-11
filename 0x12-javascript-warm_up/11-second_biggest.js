#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const item = process.argv.slice(2).map(Number);
  const item2 = item.sort(function (a, b) { return b - a; })[1];
  console.log(item2);
}
