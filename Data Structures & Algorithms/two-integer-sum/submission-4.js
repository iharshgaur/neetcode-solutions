class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        nums = nums.sort()
        let i = 0;
        let j = nums.length - 1 ;

        while ( i < j ) {
            let sum = nums[i] + nums[j]
           if( sum == target && i !== j) {
                return [i,j]
           }
           else if ( target > sum ) {
                i++
           } else {
                j--
           }
        }
    }
}
