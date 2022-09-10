#!/usr/bin/node
/* A script that prints the title of a Star Wars movie where the episode number matches a given integer */

const request = require('request');
const url = process.argv[2];
let count = 0

request(url, function (error, response, body) {
    if (error) {
	console.log(error);
    }
    JSON.parse(body).results.forEach(element => {
	element.characters.forEach(id => id.includes('18') ? count++ : count);
	return count;
    });
    console.log(count);
});
