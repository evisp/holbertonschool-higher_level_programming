#!/usr/bin/node

const numbers = process.argv;

if (numbers.length <= 3) {
  console.log('0');
} else {
  numbers.sort((a, b) => a - b);

  const numbersArray = numbers.slice(numbers.length - 2);
  console.log(numbersArray[0]);
}
