#!/usr/bin/node

const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (c) {
    const val = c;
    if (val !== undefined) {
      for (let row = 0; row < this.height; row++) {
        let str = '';
        for (let col = 0; col < this.width; col++) {
          str += val;
        }
        console.log(str);
      }
    } else {
      super.print();
    }
  }
};
