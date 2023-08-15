#!/usr/bin/node

const process = require('process');
const val = process.argv[2];
const num = parseInt(val);
let x = 0;

if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  while (x < num) {
    console.log('C is fun');
    x++;
  }
}
