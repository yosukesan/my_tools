
// code taken from: https://maku77.github.io/nodejs/io/readline-from-keyboard.html (accesed 2021/04/03)

function readUserInput(question) {
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });

  return new Promise((resolve, reject) => {
    readline.question(question, (answer) => {
      resolve(answer);
      readline.close();
    });
  });
}

(async function main() {
  const name = await readUserInput('input ');
  console.log(`Hello, ${name}!`);
})();
