#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let num = 0;
  while (num < x) {
    theFunction();
    num++;
  }
};
