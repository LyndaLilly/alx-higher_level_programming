#!/usr/bin/node

const request = require('request');
const links = process.argv[2];

request(links, function (e, response, body) {
  if (e) {
    console.log(e);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const x in tasks) {
      const task = tasks[x];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occurred. Status code: ' + response.statusCode);
  }
});
