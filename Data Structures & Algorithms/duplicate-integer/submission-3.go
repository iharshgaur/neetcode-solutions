

func hasDuplicate(nums []int) bool {
    dict := map[int]int{}
    for i := 0; i < len(nums); i++ {
        _, ok := dict[nums[i]]
        if ok {
            return true
        }
        dict[nums[i]] = 1
    }
    return false
}
