func longestConsecutive(nums []int) int {
	longestSequence := 0
	hash := make(map[int]bool)

	for i:=0; i<len(nums);i++ {
		hash[nums[i]] = true
	}

	for i:=0; i<len(nums);i++ {
		currentSequence := 1
		if !hash[nums[i] - 1]{
			for hash[nums[i] + currentSequence] {
				currentSequence+=1
			}
			longestSequence = max(longestSequence, currentSequence)
		}
	}
	return longestSequence
}