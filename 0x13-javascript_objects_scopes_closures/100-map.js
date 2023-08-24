#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map(function (num, idx) {
  return (num * idx);
});

console.log(list);
console.log(newList);
