#!/usr/bin/node

const process = require('process');
const first = process.argv[2];
const second = process.argv[3];

function add (a, b) {
  if (isNaN(parseInt(a)) || isNaN(parseInt(b))) {
    console.log(NaN);
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}
add(first, second);
