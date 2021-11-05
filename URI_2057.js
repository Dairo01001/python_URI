// var input = require('fs').readFileSync('/dev/stdin', 'utf8');
let input = `22 6 -2`;

var lines = input.split("\n");

let n = lines
  .shift()
  .split(" ")
  .map((number) => +number);

let suma = n[0] + n[1] + n[2];

if (suma < 0) {
  console.log(suma);
} else {
  console.log(suma % 24);
}
