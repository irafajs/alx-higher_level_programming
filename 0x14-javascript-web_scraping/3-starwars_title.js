#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Provide atleat one argument');
  process.exit(1);
}

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(response.statusCode);
  } else {
    const movieData = JSON.parse(body);

    console.log(`${movieData.title}`);
  }
});
