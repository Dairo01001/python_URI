var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split("\n");

let t = +lines.shift();

for (let i = 0; i < t; i++) {
  let arr = lines[i].split(" ").map((number) => +number);
  console.log(arr.reduce((suma, number) => suma + number, 0));
}
