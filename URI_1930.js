var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split("\n");


let arr = lines.shift().split(" ").map((number) => Number(number));
console.log(arr.reduce((sum, number) => sum + number, 0) - 3);
