package main
import (
	"fmt"
)

func main(){
	size := 5
	numList := make([]int, size)

	for i:=0; i<size; i++{
		fmt.Scan(&numList[i])

	}

	result := 0
	for i:=0; i<size; i++{
		result += numList[i]*numList[i]

	}
	println(result%10)
}