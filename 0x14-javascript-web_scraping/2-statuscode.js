#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node getRequestStatus.js <url-to-request>');
  process.exit(1);
}

const urlToRequest = process.argv[2];

request.get(urlToRequest, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
