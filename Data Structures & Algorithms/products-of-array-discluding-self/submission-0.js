class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length;
        const prefix = new Array(n);
        prefix[0] = 1;
        for (let i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }
        let suffix = 1;
        let sol = new Array(n)
        for (let i = n - 1; i >= 0; i--) {
            sol[i] = prefix[i] * suffix;
            suffix *= nums[i];

        }
    }}

