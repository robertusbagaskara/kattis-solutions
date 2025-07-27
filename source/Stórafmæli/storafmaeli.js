const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var inputUser = line.split(' ');
    var n = parseInt(inputUser[0]);
    
   if (n % 10) {
        console.log('Neibb');
   } else {
        console.log('Jebb');
   }
});