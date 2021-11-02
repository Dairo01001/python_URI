var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

let c = +lines.shift();

for (let i = 0; i < c; i++) {
  console.log((+lines[i] % 2 === 0 ? "0" : "1"));
}
