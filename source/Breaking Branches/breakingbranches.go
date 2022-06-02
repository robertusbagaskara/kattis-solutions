package main

import "fmt"

func main() {
	var branch int
	fmt.Scan(&branch)

	if branch%2 == 0 {
		fmt.Println("Alice")
		fmt.Println(1)
	} else {
		fmt.Println("Bob")
	}
}
