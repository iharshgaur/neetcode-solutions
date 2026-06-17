class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let left = 0;
        let right = nums.length - 1;
        console.log(nums)
        while ( left < right ) {
            let sum = nums[left] + nums[right]
            console.log({sum, left: nums[left], right: nums[right]})
            if(sum > target) right--;
            else if (sum < target) left++;
            else return [left, right]
        }
    }
}
