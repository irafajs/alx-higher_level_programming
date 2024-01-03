#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Usage: node writeToFile.js <file-path> <content-to-write>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to the file:', err);
  }
});
