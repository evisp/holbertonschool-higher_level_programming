#!/usr/bin/node

const length = parseInt(process.argv[2]);

if (isNaN(length)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < length; i++) {
    console.log('X'.repeat(length));
  }
}
