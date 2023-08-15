#!/usr/bin/node

const process = require('process');
const args = process.argv;
if (args.length === 2) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  const arr = [];
  let i = 2;
  while (i < args.length) {
    arr.push(parseInt(args[i]));
    i++;
  }
  arr.sort(function (a, b) { return b - a; });
  console.log(arr[1]);
}
