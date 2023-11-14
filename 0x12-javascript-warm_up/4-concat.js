#!/usr/bin/node

const args = process.argv;
if (args[2]) {
  console.log(args[2].concat(' is ', args[3]));
} else {
  console.log('undefined is undefined');
}
