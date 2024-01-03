#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Provide atleast one argument');
  process.exit(1);
}
const apiUrl = process.argv[2];

const wedgeAntillesId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`${response.statusCode}`);
  } else {
    const filmsData = JSON.parse(body);

    const filmsWithWedgeAntilles = filmsData.results.filter((film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`);
    });

    console.log(`${filmsWithWedgeAntilles.length}`);
  }
});
