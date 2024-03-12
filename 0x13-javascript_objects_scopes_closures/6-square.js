#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let m = 0; m < this.height; m++) {
      let y = '';
      for (let k = 0; k < this.width; k++) {
        y += c;
      }
      console.log(y);
    }
  }
}

module.exports = Square;
