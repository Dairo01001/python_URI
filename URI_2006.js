//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
let input = `4
1 2 3 2 1`;

var lines = input.split("\n");

let t = lines.shift();
let ans = lines.shift().split(" ");

console.log(ans.filter((number) => t == number).length);
