package main

import (
	"fmt"
)

var area [301][301] int
var dp [301][301] int 

func main(){
	var a, b, x, y int
	var k int
	
	setNums()
	
	fmt.Scan(&k)

	for i:=0; i < k; i++{
		fmt.Scan(&a, &b, &x, &y)
		fmt.Println(sol(a, b, x, y))
	}
}

// 차원 배열 초기값, dp 세팅
func setNums(){
	var n, m int
	fmt.Scan(&n, &m)
	for i:=1; i<n+1; i++{
		for j:=1; j <m+1; j++{
			fmt.Scan(&area[i][j])
		}
	}

	// dp 값 세팅 
	for i:=1; i<n+1; i++{
		for j:=1; j<m+1; j++{
			dp[i][j] = area[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
		}
	}
}

// dp 값 이용해서 결과값 구하기 
func sol(i int, j int, x int, y int) int {
	return dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
}