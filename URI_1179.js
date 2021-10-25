var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

lines.pop();

let arr = lines.map(number => Number(number));

let parArr = Array()
let imparArr = Array()

for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0) {
        parArr.push(arr[i]);
        if (parArr.length === 5) imprimirArr(parArr, 'par');
    } else {
        imparArr.push(arr[i]);
        if (imparArr.length === 5) imprimirArr(imparArr, 'impar');
    }
}

imprimirArr(imparArr, 'impar');
imprimirArr(parArr, 'par');

function imprimirArr(arr, name) {
    arr.forEach((element, index) => {
        console.log(`${name}[${index}] = ${element}`);
    });
    arr.length = 0;
}
