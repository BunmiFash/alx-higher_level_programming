#!/usr/bin/node

const first = process.argv[2];

if (first === undefined) {
  console.log('Not a number');
} else {
  const firstCon = parseInt(first);
  if (isNaN(firstCon) === true) {
    console.log('Not a number');
  } else {
    console.log(firstCon);
  }
}
