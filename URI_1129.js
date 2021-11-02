//var input = require("fs").readFileSync("/dev/stdin", "utf8");
let input = `3
0 255 255 255 255
255 255 255 255 0
255 255 127 255 255
4
200 200 200 0 200
200 1 200 200 1
1 2 3 4 5
255 5 200 130 205
0`;

var lines = input.split("\n");

let resp = ["A", "B", "C", "D", "E"];

while (true) {
  n = Number(lines.shift());
  if (!n) break;

  while (n--) {
    let puntos = lines
      .shift()
      .split(" ")
      .map((number) => Number(number));
    let count = 0;
    let pos = -1;
    for (let i = 0; i < puntos.length; i++) {
      if (puntos[i] <= 127) {
        count++;
        pos = i;
      }
    }
    if (count > 1 || pos == -1) {
      console.log("*");
    } else {
      console.log(resp[pos]);
    }
  }
}
