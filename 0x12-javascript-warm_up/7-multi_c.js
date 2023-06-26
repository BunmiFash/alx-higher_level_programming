#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (num === undefined || isNaN(num) === true) {
  console.log('Missing number of occurrences');
}
let count;
for (count = 0; count < num; count++) {
  console.log('C is fun');
}
