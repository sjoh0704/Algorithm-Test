package main

import (
	"fmt"
)

func calculate(number int) int {
	num1 := number / 10
	num2 := number % 10
	sum := num1 + num2
	return num2*10 + sum%10

}
func main() {
	var N int
	fmt.Scanln(&N)
	count := 0
	result := N
	for true {
		count++
		result = calculate(result)
		if N == result {
			fmt.Println(count)
			break
		}
	}
}
