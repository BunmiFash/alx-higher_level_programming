#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

const one = [];
const two = [];
const three = [];

for (const key in dict) {
  if (dict[key] === 1) {
    one.push(key);
  } else if (dict[key] === 2) {
    two.push(key);
  } else {
    three.push(key);
  }
}
newDict['1'] = one;
newDict['2'] = two;
newDict['3'] = three;

console.log(newDict);
