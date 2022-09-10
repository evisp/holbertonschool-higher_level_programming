#!/usr/bin/node
/* A script that gets the contents of a webpage and stores it in a file. */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) {
	console.log(error);
    }
    const json = JSON.parse(body);
    const completed_tasks = {}
    for (const user of json) {
	const id = user.userId;
	if (user.completed) {
	    if (completed_tasks[id]) {
		completed_tasks[id] += 1;
	    } else {
		completed_tasks[id] = 1;
	    }
	}
    }
    console.log(completed_tasks)
});
