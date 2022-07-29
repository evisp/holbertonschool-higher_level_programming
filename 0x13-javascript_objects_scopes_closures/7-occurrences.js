#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {

    const counter = list.reduce((count, el) => (el === searchElement ? count + 1 : count), 0);
    return counter;
};
