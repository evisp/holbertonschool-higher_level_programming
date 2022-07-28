#!/usr/bin/node

let count = parseInt(process.argv[2]);

if (isNaN(count)) {
  console.log('Missing number of ocurrences');
} else {
  while (count-- > 0) {
    console.log('C is fun');
  }
}
