#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof (w) === 'number' && typeof (h) === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let str = '';
      for (let col = 0; col < this.width; col++) {
        str += 'X';
      }
      console.log(str);
    }
  }
};
