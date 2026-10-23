func productExceptSelf(nums []int) []int {
	op := []int{}
	length := len(nums)
	leftProducts := make([]int, length)
	rightProducts := make([]int, length)

	runningProduct:=1
	for i:=0;i<len(nums);i++{
		runningProduct= runningProduct * nums[i]
		leftProducts[i]= runningProduct
	}

	runningProduct=1
	for i:=len(nums) - 1;i>=0;i--{
		runningProduct= runningProduct * nums[i]
		rightProducts[i] = runningProduct
	}

	for i:=0;i<len(nums);i++{
		if i==0 {
			op = append(op,rightProducts[i+1])
		} else if i == len(nums) - 1{
			op = append(op,leftProducts[i-1])
		} else {
		op = append(op, leftProducts[i-1] * rightProducts[i+1])
		}
	}
	return op
}
