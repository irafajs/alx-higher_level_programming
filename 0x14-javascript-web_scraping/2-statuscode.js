#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('provide altleat 1 argumnet');
  process.exit(1);
}

const urlToRequest = process.argv[2];

request.get(urlToRequest, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
