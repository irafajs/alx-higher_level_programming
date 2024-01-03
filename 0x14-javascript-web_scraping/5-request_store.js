#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Provide at least 2 arguments>');
  process.exit(1);
}

const urlToRequest = process.argv[2];
const filePathToStore = process.argv[3];

request.get(urlToRequest, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`${response.statusCode}`);
  } else {
    fs.writeFile(filePathToStore, body, 'utf8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      }
    });
  }
});
