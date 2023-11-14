#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
