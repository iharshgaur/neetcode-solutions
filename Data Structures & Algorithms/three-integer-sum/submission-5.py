class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        s_nums = sorted(nums)

        for i in range(0, len(s_nums) - 2):
            if i > 0 and s_nums[i] == s_nums[i - 1]:
                continue
            j = i + 1
            k = len(s_nums) - 1
            while(j < k):
                _sum = s_nums[i] + s_nums[j] + s_nums[k]
                if _sum == 0:
                    res.append([s_nums[i], s_nums[j], s_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and s_nums[j] == s_nums[j-1]:
                        j += 1
                    while j < k and s_nums[k] == s_nums[k+1]:
                        k -= 1
                elif _sum > 0:
                    k -= 1
                else:
                    j += 1
        return res