package main

import "fmt"

func main() {
	var w, b int = 0, 0
	var stones string
	fmt.Scan(&stones)

	for i := 0; i < len(stones); i++ {
		if stones[i] == 'W' {
			w = w + 1
		} else {
			b = b + 1
		}
	}
	if w == b {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}
