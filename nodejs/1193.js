const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input = [];
rl.on("line", function(line) {
    input.push(Number(line));    
}).on("close", function() {
    sol(input);
    process.exit();
});
const sol = (data)=>{
    let x = data[0];
    let i = 1;
    let sum = 1;
    while (true){
        if(sum > x){
            sum-=--i;
            break;
        }
        else{
            sum += i++;
        }
    }
    let left = 1;
    let right = i;
    let diff = x - sum;
    let ans;
    if(i%2 === 0){
        ans = (left + diff) + "/" + (right - diff)
    }
    else{
        ans = (right - diff) + "/" + (left + diff) 
    }
    console.log(ans);
};