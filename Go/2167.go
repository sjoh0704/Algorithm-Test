package main

import (
	"fmt"
)
var dp [301][301] int 

func main(){
	var a, b, x, y int
	var k int
	setNums()
	fmt.Scan(&k)
	result := make([]int, k)
	
	for i:=0; i < k; i++{
		fmt.Scan(&a, &b, &x, &y)
		result[i] = sol(a, b, x, y)
	}
	
	for i:=0; i<k; i++{
		fmt.Println(result[i])
	}

}

func setNums(){
	var n, m int
	fmt.Scan(&n, &m)
	for i:=1; i<n+1; i++{
		for j:=1; j <m+1; j++{
			var tmp int
			fmt.Scan(&tmp)
			for k:= i; k < n+1; k++{
				for l:=j; l < m+1; l++{
					dp[k][l] += tmp
				}
			}
		}
	}
}

func sol(a int, b int, x int, y int) int {
	sum := dp[x][y] - dp[x][b-1] - dp[a-1][y] + dp[a-1][b-1]
	return sum
}