const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
   
readline.question('Enter Input: ', text => {
    console.log(`Typed Text: ${text}`);
    readline.close();
});