#!/usr/bin/node
// Writes to a file

const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error('Error writing to file:', err);
    } else {
      console.log(`Successfully wrote content to ${filePath}`);
    }
  });
}

// Check if the required arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node writeToFile.js <file-path> <content-to-write>');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeToFile(filePath, content);
}
