package main

import (
	"fmt"
)

func main(){
	a, b, v := getInputs()
	result := sol(a, b, v)
	fmt.Println(result)
}

// 입력 받기 
func getInputs() (int, int ,int){
	var a, b, v int
	fmt.Scan(&a, &b, &v)
	return a, b, v
}

// 올라가는데 며칠이 걸리는데 계산
func sol(a int, b int, v int) int {
	
	v -= a  // 정상에 올라가서 미끄러지지 않는 경우를 먼저 제외 
	ans := 1  // 미끄러지지 않는 경우를 제외했으므롤 초기 값 1
	ans += v / (a-b)  // 미끄러지는 경우 

	// 미끄러지지 않는 횟수가 나누어 떨어지지 않는 경우 +1 
	if float64(v) / float64(a-b) - float64(int(float64(v) / float64(a-b))) != 0 {
		ans += 1
	}

	return ans
}