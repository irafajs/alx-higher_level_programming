#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Please provide the Movie ID as an argument');
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
        const characterUrls = movieData.characters;

        function fetchAndPrintCharacter (index) {
          if (index < characterUrls.length) {
            const characterUrl = characterUrls[index];
            request.get(characterUrl, (charError, charResponse, charBody) => {
              if (!charError && charResponse.statusCode === 200) {
                const characterData = JSON.parse(charBody);
                console.log(characterData.name);
                fetchAndPrintCharacter(index + 1);
              } else {
                console.error(`${charResponse.statusCode}`);
              }
            });
          }
        }

        console.log(`${movieData.title}`);
        fetchAndPrintCharacter(0);
      } else {
        console.log(`No characters found for the movie with ID ${movieId}`);
      }
    } catch (parseError) {
      console.error(`Error: Unable to parse JSON response - ${parseError}`);
    }
  }
});
