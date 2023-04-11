#!/usr/bin/node

const parseNo = parseInt(process.argv[2]);
if (isNaN(parseNo)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseNo);
}
