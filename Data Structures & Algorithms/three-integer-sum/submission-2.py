class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for i in range(0,len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    result.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                elif _sum < 0:
                    j += 1
                else:
                    k -= 1
        return [list(x) for x in result]