const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input = [];
rl.on("line", function(line) {
    let num = line.split(" ")[0];
    if(num === "0"){
        rl.close();
    }
    input.push(num);
}).on("close", function() {
    sol(input);
    process.exit();
});

const sol = (data) =>{
    data.forEach(e => {
        let FLAG = true;
        for(let i=0; i < parseInt(e.length/2); i++){
            if(e[i] !== e[e.length-i-1]){
                FLAG = false;
                break;
            }
        }
        if(FLAG){
            console.log("yes");
        }else{
            console.log("no");
        }
    });
}

