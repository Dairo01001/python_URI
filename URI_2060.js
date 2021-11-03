//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
let input = `5
2 5 4 20 10`;

var lines = input.split("\n");

let n = +lines.shift();
let l = lines
  .shift()
  .split(" ")
  .map((number) => +number);

let countTwo = 0;
let countThree = 0;
let countFour = 0;
let countFive = 0;

l.forEach((value) => {
  if (value % 2 === 0) countTwo++;
  if (value % 3 === 0) countThree++;
  if (value % 4 === 0) countFour++;
  if (value % 5 === 0) countFive++;
});

console.log(`${countTwo} Multiplo(s) de 2`);
console.log(`${countThree} Multiplo(s) de 3`);
console.log(`${countFour} Multiplo(s) de 4`);
console.log(`${countFive} Multiplo(s) de 5`);
