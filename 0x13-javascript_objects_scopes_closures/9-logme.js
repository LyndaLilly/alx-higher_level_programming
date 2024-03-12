#!/usr/bin/node
let argu = 0;

exports.logMe = function (item) {
  console.log(argu + ': ' + item);
  argu++;
};
