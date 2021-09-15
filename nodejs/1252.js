const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input = [];
rl.on("line", function(line) {
    input.push(line.split(" "));
}).on("close", function() {
    sol(input);
    process.exit();
});

const sol = (data) =>{
    const [a, b] = data[0];
    let long, short; 
    if(a.length > b.length){
        long = a;
        short = b;
    }
    else{
        long = b;
        short = a;
    }
    result = "";
    reverse_long = reverseStr(long);
    reverse_short = reverseStr(short);

    for(let i=0; i< short.length; i++){
        let sum = Number(reverse_long[i])+ Number(reverse_short[i]);
        result = sum + result;
    }
    result = long.slice(0, long.length - short.length) + result;
    ans = "";
    let add = 0;
    for(let i=result.length-1; i >=0 ; i--){
        let tmp = Number(result[i]);

        if(tmp+add >= 2){
            ans = (tmp+add-2) + ans;
            add = 1;
        }
        else{
            ans = (tmp + add) + ans;
            add = 0;
        }

        if(i == 0 && tmp + add >= 2){
            ans = 1 + ans;
        }

    }
    let check = ""
    for(let i=0; i<ans.length;i++){
        if(Number(ans[i]) === 1){
            check += ans.slice(i);
            break;
        }
        if(Number(ans[i]) !== 0){
            check += ans[i];
        }
    }
    if(check == ""){
        console.log(0);
    }
    else{
        console.log(check);
    }
}
const reverseStr = str =>{
    let result = ""
    for(let i =0; i<str.length; i++){
        result = str[i] + result; 
    }
    return result;
}
