func groupAnagrams(strs []string) [][]string {
	globalHash := map[[26]int][]string{}

	for i := 0; i < len(strs); i++ {
		dict := createDictionary(strs[i])
		globalHash[dict] = append(globalHash[dict], strs[i])
	}

	op := [][]string{}

	for _, v := range globalHash {
		op = append(op, v)
	}
	return op
}

func createDictionary(str string) [26]int {
	dict := [26]int{}

	for i := 0; i < len(str); i++ {
		dict[str[i]-'a']++
	}

	return dict
}