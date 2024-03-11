#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const m = Number(process.argv[2]);
  let n = 0;
  while (m < n) {
    console.log('X'.repeat(m));
    n++;
  }
}
