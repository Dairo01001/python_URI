var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const O = lines.shift();

const size = 12;
let i, j;

m = new Array(size);
for (i = 0; i < size; i++) {
    m[i] = new Array(size);
}

let count = 0;
for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
        m[i][j] = Number(lines[count++]);
    }
}

count = 0;
let suma = 0;
let yFinal = size;
let yInicial = 0;
for (i = 0; i < 5; i++) {
    yFinal--;
    yInicial++;
    for (j = yInicial; j < yFinal; j++) {
        suma += m[i][j];
        count++;
    }
}

console.log((O === 'S' ? suma.toFixed(1) : (suma / count).toFixed(1)));