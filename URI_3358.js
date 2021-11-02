var input = require("fs").readFileSync("/dev/stdin", "utf8");
var lines = input.split("\n");

let N = +lines.shift();

for (let i = 0; i < N; i++) {
  let name = lines[i].toLowerCase();
  let x = 0;
  let isFacil = true;
  while (x < name.length) {
    if (notIsVocal(name.charAt(x))) {
      let count = 1;
      x++;
      while (notIsVocal(name.charAt(x)) && x < name.length) {
        count++;
        x++;
      }
      if (count >= 3) {
        isFacil = false;
        break;
      }
    }
    x++;
  }
  if (isFacil) {
    console.log(`${lines[i]} eh facil`);
  } else {
    console.log(`${lines[i]} nao eh facil`);
  }
}

function notIsVocal(char) {
  return !(
    char == "a" ||
    char == "e" ||
    char == "i" ||
    char == "o" ||
    char == "u"
  );
}
