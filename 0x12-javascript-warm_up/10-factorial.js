#!/usr/bin/node

function factorial (a) {
  a = parseInt(process.argv[2]);
  if (isNaN(a)) {
    console.log(1);
  } else {
    let fact = 1;
    for (let i = 1; i <= a; i++) {
      fact *= i;
      console.log(fact);
    }
  }
}
factorial();
