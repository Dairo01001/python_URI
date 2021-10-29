var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const O = lines.shift();
const size = 12;

let i, j;
let m = new Array(size);
for (i = 0; i < size; i++) {
    m[i] = new Array(size);
}

let count = 0;

for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
        m[i][j] = Number(lines[count++]);
    }
}

let x = size;
let suma = 0;
count = 0;
for (j = 0; j < size; j++) {
    for (i = x; i < size; i++) {
        suma += m[i][j];
        count++;
    }
    x--;
}

console.log((O === 'S' ? suma.toFixed(1) : (suma / count).toFixed(1)));
