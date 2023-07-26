#!/usr/bin/node
// reads a file

const fs = require('fs');

function readAndPrintFile (filePath) {
  fs.readFile(filePath, 'utf-8', (err, content) => {
    if (err) {
      console.error('An error occurred while reading the file:');
      console.error(err);
    } else {
      console.log(content);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <file_path>');
} else {
  const filePath = process.argv[2];
  readAndPrintFile(filePath);
}
