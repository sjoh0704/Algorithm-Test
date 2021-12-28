package main

import (
	"fmt"
	"strconv"
)

func main(){

	var input int
	var result []string
	
	// 입력 받기 
	fmt.Scanln(&input)
	for input != -1{
		tmp := sol(input)
		result = append(result, tmp)
		fmt.Scanln(&input)
	}

	for _, v:= range result{
		fmt.Println(v)
		
	}
}
	
// 완전수 체크 
func sol(pn int) string {

	//str 초기 세팅 
	str := strconv.Itoa(pn) +" = "
	sum := 0
	for i:=1; i<pn; i++{
		if pn % i == 0{
			sum += i
			str += strconv.Itoa(i) + " + " 
		}
	} 

	if sum != pn{
		// 완전수가 아닐때 
		str = strconv.Itoa(pn) + " is NOT perfect"
	}else{
		// 완전수 일때 
		str = str[:len(str) - 3]
	}
	
	return str
}