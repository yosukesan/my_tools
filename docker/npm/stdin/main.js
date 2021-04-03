
// code taken from: https://qiita.com/zenrshon/items/2fcc8d6a01c81fe7b2cd (accesed 2021/04/03)

process.stdin.resume();
process.stdin.setEncoding('utf8');

var input_lines = [];
var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

reader.on('close', () => {
  console.log(input_lines);
});
