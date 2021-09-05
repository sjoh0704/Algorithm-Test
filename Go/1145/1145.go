package main

import (
	"fmt"
)

func main() {
	var numbers []int = make([]int, 5)
	for i := 0; i < 5; i++ {
		fmt.Scan(&numbers[i])
	}
	ans := 0
	for {
		check := 0
		ans++
		for i := 0; i < 5; i++ {
			if ans%numbers[i] == 0 {
				check++
			}
		}
		if check >= 3 {
			fmt.Println(ans)
			break
		}
	}
}
