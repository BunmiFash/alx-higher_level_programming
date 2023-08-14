#!/usr/bin/node

const process = require('process');
const args = process.argv;
const first = args[2];
const second = args[3];

console.log(first + ' ' + 'is' + ' ' + second);
