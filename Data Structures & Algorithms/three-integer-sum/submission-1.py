class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(0,len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    result.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1
        return result