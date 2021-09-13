const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input = [];
rl.on("line", function(line) {
    input.push(line.split(""));
}).on("close", function() {
    sol(input);
    process.exit();
});
const find = (area, N, M) =>{
    let row = 0;
    let col = 0;
    for(let i=0; i<N; i++){
        let FLAG = true;
        for(let j=0; j <M; j++){
            if(area[i][j] === "X"){
                FLAG = false;
                break;
            }
        }
        if(FLAG){
            row++;
        }
    }
    for(let i=0; i<M; i++){
        let FLAG = true;
        for(let j=0; j <N; j++){
            if(area[j][i] === "X"){
                FLAG = false;
                break;
            }
        }
        if(FLAG){
            col++;
        }
    }
    return Math.max(col, row);

}

const sol = (data)=>{
    const [N, _, M] = data[0];
    let area = data.slice(1);
    console.log(find(area, N, M));
};