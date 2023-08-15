#!/usr/bin/node

const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);
let row = 0;

if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (row < num) {
    const arr = [];
    let col = 0;
    while (col < num) {
      arr.push('X');
      col++;
    }
    console.log(arr.join(''));
    row++;
  }
}
