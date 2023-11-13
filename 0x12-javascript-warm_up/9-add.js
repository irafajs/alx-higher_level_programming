#!/usr/bin/node

function add (a, b) {
  const arg = process.argv;
  a = parseInt(arg[2]);
  b = parseInt(arg[3]);
  if (isNaN(a) || isNaN(b)) {
    console.log(NaN);
  } else {
    console.log(a + b);
  }
}
add();
