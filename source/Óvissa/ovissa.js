const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

const rl = readline.createInterface({ input, output });

rl.on('line', (line) => {
    var unnarSound = line ;
    var uCounter = 0

    for (let i=0; i < unnarSound.length; i++) {
        if (unnarSound[i] == "u") {
            uCounter += 1;
        }
    };

    console.log(uCounter);

    rl.close();
});