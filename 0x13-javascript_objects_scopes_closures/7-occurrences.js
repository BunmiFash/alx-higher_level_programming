#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let num = 0;

  for (let i = 0; i < len; i++) {
    if (searchElement === list[i]) {
      num += 1;
    }
  }
  return (num);
};
