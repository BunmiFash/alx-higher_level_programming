#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size === undefined || isNaN(size) === true) {
  console.log('Missing size');
}

let row;
let col;
for (row = 0; row < size; row++) {
  for (col = 0; col < size; col++) {
    process.stdout.write('X');
  }
  console.log('');
}
