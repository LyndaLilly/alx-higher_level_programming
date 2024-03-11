#!/usr/bin/node
function isfactorial (x) {
  if (x < 0) {
    return (-1);
  }
  if (x === 0 || isNaN(x)) {
    return (1);
  }
  return (x * isfactorial(x - 1));
}

console.log(isfactorial(Number(process.argv[2])));
