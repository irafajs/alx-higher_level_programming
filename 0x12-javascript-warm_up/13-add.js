#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return undefined;
  } else {
    return (a + b);
  }
}
module.exports = { add };
