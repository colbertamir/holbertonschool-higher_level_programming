#!/usr/bin/node
const parsedValue = parseInt(process.argv[2]);

if (isNaN(parsedValue)) {
  console.log('Not a number');
} else {
  console.log('My number:', parsedValue);
}
