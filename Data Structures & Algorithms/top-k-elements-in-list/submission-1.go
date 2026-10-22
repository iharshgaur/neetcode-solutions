func topKFrequent(nums []int, k int) []int {
	op := []int{}
	occ := map[int]int{}

	for i := 0; i < len(nums); i++ {
		occ[nums[i]]++
	}

	buckets := make([][]int, len(nums)+1)
	for num, occurence := range occ {
		buckets[occurence] = append(buckets[occurence], num)
	}

	for i := len(buckets) - 1; i >= 0 && len(op) < k; i-- {
		for _, num := range buckets[i] {
			op = append(op, num)
			if len(op) == k {
				break
			}
		}
	}

	return op
}