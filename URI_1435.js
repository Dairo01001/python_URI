//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
let input = `1
2
3
4
5
0`;

var lines = input.split('\n');
const arr = lines.map((number) => { return +number });

arr.forEach((number) => {
    if (!number) return;
    let mid = Math.ceil(number / 2);

    const m = new Array(number);
    for (let i = 0; i < number; i++) {
        m[i] = new Array(number);
    }

    for (let i = 0; i < mid; i++) {
        let bot = number - 1 - i;

        for (let j = 0; j <= bot; j++) {
            m[i][j] = i + 1;
            m[bot][j] = i + 1;
            m[j][i] = i + 1;
            m[j][bot] = i + 1;
        }
    }

    for (let i = 0; i < number; i++) {
        let str = "";
        for (let j = 0; j < number; j++) {
            str += m[i][j] + "   ";
        }
        console.log(str);
    }

});

