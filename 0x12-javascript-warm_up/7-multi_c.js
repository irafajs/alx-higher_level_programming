#!/usr/bin/node

const arrayStr = 'C is fun';
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log(arrayStr);
  }
}
