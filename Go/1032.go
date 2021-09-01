package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	var words []string = make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&words[i])
	}

	var firstWord string = words[0]
	var ans string = ""
	for i := 0; i < len(firstWord); i++ {
		FLAG := true
		for j := 1; j < n; j++ {
			if firstWord[i] != words[j][i] {
				FLAG = false
				break
			}

		}
		if FLAG {
			ans += string(firstWord[i])
		} else {
			ans += "?"
		}
	}

	fmt.Println(ans)

}
