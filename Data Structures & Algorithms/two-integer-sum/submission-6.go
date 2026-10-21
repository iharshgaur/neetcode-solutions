func twoSum(nums []int, target int) []int {
	hash := map[int]int{}

	for i:=0;i<len(nums);i++{
		hash[nums[i]] = i
	}

	for k,v := range nums {
		j,has_diff := hash[target - v]
		if has_diff && k != j {
			return []int{k, j}
		}
	}
	return nil
}
