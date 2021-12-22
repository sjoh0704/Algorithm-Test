package main

import (
	"fmt"
)

func main(){
	
	var nums [10]int
	var inputs [3]int
	
	//입력
	fmt.Scan(&inputs[0])
	fmt.Scan(&inputs[1])
	fmt.Scan(&inputs[2])

	//연산
	str_mul := inputs[0] * inputs[1] * inputs[2]

	// 더이상 남는 숫자가 없을 때까지 반복 
	for str_mul >= 1{
		tmp:= str_mul%10
		nums[tmp] += 1
		str_mul /= 10
	}

	// 출력
	for i:= 0; i < 10; i++{
		fmt.Println(nums[i])
	}

}