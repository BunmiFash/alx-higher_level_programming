#!/usr/bin/node

const args = process.argv;
const first = args[2];

if (first === undefined) {
  console.log('No argument');
} else {
  console.log(first);
}
