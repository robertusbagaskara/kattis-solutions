package main

import "fmt"

func main() {
	var s string
	fmt.Scanln(&s)
	flag := false
	for i := 0; i < len(s); i++ {
		if s[i] == 'a' {
			flag = true
		}
		if flag {
			fmt.Printf("%c", s[i])
		}

	}
}
