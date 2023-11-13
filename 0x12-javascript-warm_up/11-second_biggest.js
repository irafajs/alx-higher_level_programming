#!/usr/bin/node

const args = process.argv;
let firstLargest = Number.MIN_SAFE_INTEGER;
let secondLargest = Number.MIN_SAFE_INTEGER;

if (args.length <= 3) {
  console.log(0);
} else {
  for (let c = 2; c < args.length; c++) {
    const currentNumber = parseInt(args[c]);

    if (!isNaN(currentNumber)) {
      if (currentNumber > firstLargest) {
        secondLargest = firstLargest;
        firstLargest = currentNumber;
      } else if (currentNumber > secondLargest && currentNumber !== firstLargest) {
        secondLargest = currentNumber;
      }
    }
  }

  console.log(secondLargest);
}
