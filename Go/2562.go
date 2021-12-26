package main

import (
	"fmt"
)

func main(){
	size := 9
	numList := make([]int, size)
	for i:=0; i< size; i++{
		fmt.Scan(&numList[i])
	}
	maxIdx := findMaxIdx(numList)
	fmt.Println(numList[maxIdx]) // 최댓값 출력
	fmt.Println(maxIdx+1) // 최댓값이 몇번째 값인지 출력
}

func findMaxIdx(numList []int) (int){
	// 최댓값을 갖는 인덱스를 리턴하는 함수 
	maxIdx := 0
	for i:= 1; i<len(numList); i++{
		if numList[maxIdx] < numList[i]{
			maxIdx = i
		} 
	}
	return maxIdx
}