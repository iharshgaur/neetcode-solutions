func isAnagram(s string, t string) bool {
	dic1 := map[uint8]int{}
	dic2 := map[uint8]int{}

	if len(s) != len(t) {
		return false
	}

	for i:=0;i<len(s);i++{
		dic1[s[i]]++
		dic2[t[i]]++
	}

	for k, v := range dic1 {
		if v != dic2[k] {
			return false
		}
	}


	return true
}

