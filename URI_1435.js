var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

const arr = lines.map((number) => {
  return Number(number);
});

const m = new Array(100);
for (let i = 0; i < 100; i++) {
  m[i] = new Array(100);
}

arr.forEach((number) => {
  if (!number) return;

  for (let i = 0; i < number; i++) {
    let botI = number - 1 - i;
    for (let j = i; j < number - i; j++) {
      let botJ = number - 1 - j;
      m[i][j] = i + 1;
      m[j][i] = i + 1;

      m[botI][botJ] = i + 1;
      m[botJ][botI] = i + 1;
    }
  }

  for (let i = 0; i < number; i++) {
    let str = "";
    for (let j = 0; j < number; j++) {
      if (j === 0) {
        str += m[i][j];
      } else {
        str += "   " + m[i][j];
      }
    }
    console.log(str);
  }
  console.log("");
});
