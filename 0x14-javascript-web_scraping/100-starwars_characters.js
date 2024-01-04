#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('provide atleast one argument');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);

      if (movieData.characters && movieData.characters.length > 0) {
        console.log(`${movieData.title}`);

        movieData.characters.forEach((characterUrl) => {
          request.get(characterUrl, (charError, charResponse, charBody) => {
            if (!charError && charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
            } else {
              console.error(`Error fetching character data (Status code: ${charResponse.statusCode})`);
            }
          });
        });
      } else {
        console.log(`No characters found for the movie with ID ${movieId}`);
      }
    } catch (parseError) {
      console.error(`Error: Unable to parse JSON response - ${parseError}`);
    }
  }
});
