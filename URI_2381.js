//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
let input = `5 3
maria
joao
carlos
vanessa
jose`;

var lines = input.split('\n');

let nk  = lines.shift().split(' ').map((value) => Number(value));

console.log(lines.sort()[nk[1] - 1]);
