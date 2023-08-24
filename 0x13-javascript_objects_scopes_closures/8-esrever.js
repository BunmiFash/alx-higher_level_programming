#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  const len = list.length;

  for (let i = 0; i < len; i++) {
    rev.unshift(list[i]);
  }
  return rev;
};
