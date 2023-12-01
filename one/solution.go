package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"runtime"
	"strconv"
)

func getParams(regEx, url string) (paramsMap map[string]string) {
	var compRegEx = regexp.MustCompile(regEx)
	match := compRegEx.FindStringSubmatch(url)

	paramsMap = make(map[string]string)
	for i, name := range compRegEx.SubexpNames() {
		if i > 0 && i <= len(match) {
			paramsMap[name] = match[i]
		}
	}
	return paramsMap
}

func main() {
	// current file's directory
	_, currentFile, _, _ := runtime.Caller(0)
	currentDir := filepath.Dir(currentFile)
	joinedPath := filepath.Join(currentDir, "input.txt")

	// open the file and defer closing
	file, err := os.Open(joinedPath)
	if err != nil {
		log.Fatal("couldn't open input.txt file", err)
		return
	}
	defer file.Close()

	var firstPartSum = 0
	var secondPartSum = 0

	// scan line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		firstDigitRe := `(?P<FirstDigit>\d)`
		firstDigitParams := getParams(firstDigitRe, line)
		firstDigit := firstDigitParams["FirstDigit"]

		lastDigitRe := `.*(?P<LastDigit>\d)`
		lastDigitParams := getParams(lastDigitRe, line)
		lastDigit := lastDigitParams["LastDigit"]

		twoDigitStr := firstDigit + lastDigit
		twoDigitNum, err := strconv.Atoi(twoDigitStr)
		if err != nil {
			log.Fatal("error converting number", err)
			return
		}

		firstPartSum += twoDigitNum

		// part two

		var digitsMap = map[string]string{
			"1":     "1",
			"one":   "1",
			"2":     "2",
			"two":   "2",
			"3":     "3",
			"three": "3",
			"4":     "4",
			"four":  "4",
			"5":     "5",
			"five":  "5",
			"6":     "6",
			"six":   "6",
			"7":     "7",
			"seven": "7",
			"8":     "8",
			"eight": "8",
			"9":     "9",
			"nine":  "9",
		}

		partTwoFirstDigitRe := `(?P<FirstDigit>\d|one|two|three|four|five|six|seven|eight|nine)`
		partTwoFirstDigitParams := getParams(partTwoFirstDigitRe, line)
		partTwoFirstDigitRaw := partTwoFirstDigitParams["FirstDigit"]
		partTwoFirstDigit := digitsMap[partTwoFirstDigitRaw]

		partTwoLastDigitRe := `.*(?P<LastDigit>\d|one|two|three|four|five|six|seven|eight|nine)`
		partTwoLastDigitParams := getParams(partTwoLastDigitRe, line)
		partTwoLastDigitRaw := partTwoLastDigitParams["LastDigit"]
		partTwoLastDigit := digitsMap[partTwoLastDigitRaw]

		partTwoTwoDigitStr := partTwoFirstDigit + partTwoLastDigit
		partTwoTwoDigitNum, err := strconv.Atoi(partTwoTwoDigitStr)
		if err != nil {
			log.Fatal("error converting number", err)
			return
		}

		secondPartSum += partTwoTwoDigitNum

		//fmt.Printf("line=%v, first=%v, last=%v\n", line, firstDigit, lastDigit)
	}

	fmt.Printf("first part sum=%v\n", firstPartSum)
	fmt.Printf("second part sum=%v\n", secondPartSum)

	// log any scanning issues
	if err := scanner.Err(); err != nil {
		log.Fatal("an error happened during scanning input.txt line by line", err)
		return
	}
}
