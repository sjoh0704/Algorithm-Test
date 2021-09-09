const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

rl.on("line", function(line) {
    input.push(line.split(" ").map(item => Number(item)));

}).on("close", function() {
    sol(input);
    process.exit();
});

const sol = (data)=>{
    const N = data[0][0];
    let maxGrade = Math.max(...data[1]) ;
    let fakeGrades = data[1].map(grade => grade/maxGrade*100)
    let sum = 0;
    fakeGrades.forEach(grade=>{
        sum += grade;
    })
    let average = sum / N;
    console.log(average);
}