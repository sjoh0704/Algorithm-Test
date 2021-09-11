const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input = [];
rl.on("line", function(line) {
    input.push(line)
}).on("close", function() {
    sol(input);
    process.exit();
});
const sol = (data)=>{
    let dic = {};
    data[0].split("").forEach(e=> {
        let num = e.charCodeAt(0); 
        if(num > 96){
            num -= 32;
        }
        if(dic[num]){
            dic[num] += 1;
        }else{
            dic[num] = 1;
        }
    });
    let maxKey = null;
    let maxTmp = 0;
    for(let key in dic){
        if(dic[key] > maxTmp){
            maxTmp = dic[key];
            maxKey = key;
        }
    }
    let cnt = 0;
    for(let key in dic){
        if(dic[key] == dic[maxKey]){
            cnt += 1;
        }
    }

    if(cnt === 1){
        console.log(String.fromCharCode(maxKey));
    }
    else{
        console.log("?");
    }

};