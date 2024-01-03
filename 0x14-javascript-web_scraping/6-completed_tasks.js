#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('provide at least one argument');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`${response.statusCode}`);
  } else {
    const tasksData = JSON.parse(body);

    const completedTasksByUser = {};

    tasksData.forEach((task) => {
      if (task.completed) {
        completedTasksByUser[task.userId] = (completedTasksByUser[task.userId] || 0) + 1;
      }
    });

    const maxKeyLength = Math.max(...Object.keys(completedTasksByUser).map(key => key.length));

    const resultString = Object.entries(completedTasksByUser).reduce((acc, [key, value], index, array) => {
      const lineEnding = index === array.length - 1 ? ' ' : ',\n';
      const indentation = ' '.repeat(maxKeyLength - key.length + 1);
      return `${acc} '${key}':${indentation}${value}${lineEnding}`;
    }, '');

    console.log(`{${resultString}}`);
  }
});
