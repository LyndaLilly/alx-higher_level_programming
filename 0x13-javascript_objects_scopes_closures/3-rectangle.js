#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let m = 0; m < this.height; m++) {
      let y = '';
      for (let k = 0; k < this.width; k++) {
        y += 'X';
      }
      console.log(y);
    }
  }
}

module.exports = Rectangle;
