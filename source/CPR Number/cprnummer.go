package main

import (
	"fmt"
	"strconv"
)

func main() {
	code_num := [...]int{4, 3, 2, 7, 6, 5, 0, 4, 3, 2, 1}
	var cpr string
	tmp := 0
	fmt.Scanln(&cpr)
	for i := 0; i < len(cpr); i++ {
		if cpr[i] == '-' {
			continue
		} else {
			num, _ := strconv.Atoi(string(cpr[i]))
			tmp += num * code_num[i]
		}
	}
	if tmp%11 == 0 {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}
