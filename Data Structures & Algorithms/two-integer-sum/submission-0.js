class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        nums.sort((a,b) => a-b)
        let left = 0;
        let right = nums.length - 1;

        while ( left < right ) {
            let sum = nums[left] + nums[right]
            if(sum > target) right--;
            else if (sum < target) left++;
            else return [left, right]
        }
    }
}
