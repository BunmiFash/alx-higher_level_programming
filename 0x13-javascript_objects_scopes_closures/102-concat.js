#!/usr/bin/node

const fs = require('fs');

const first = process.argv[2];
const second = process.argv[3];
const third = process.argv[4];

if (
  fs.existsSync(first) &&
    fs.statSync(first).isFile &&
    fs.existsSync(second) &&
    fs.statSync(second).isFile &&
    third !== undefined
) {
  const firstthirdontent = fs.readFileSync(first);
  const secondthirdontent = fs.readFileSync(second);
  const stream = fs.createWriteStream(third);

  stream.write(firstthirdontent);
  stream.write(secondthirdontent);
  stream.end();
}
