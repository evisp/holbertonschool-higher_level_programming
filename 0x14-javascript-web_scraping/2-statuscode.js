#!/usr/bin/node
/* A script that writes a string to a file. */

const request = require('request');

request.get(process.argv[2]).on('response', function (response) {
  console.log('code:', response.statusCode);
});
