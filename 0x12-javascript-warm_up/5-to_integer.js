#!/usr/bin/node

const process = require('process');
const args = process.argv;
const first = parseInt(args[2]);

if (isNaN(first)) {
  console.log('Not a Number');
} else {
  console.log('My number:  ' + first);
}
