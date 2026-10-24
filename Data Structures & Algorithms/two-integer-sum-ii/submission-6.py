class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        op = []
        i = 0
        j = len(numbers) - 1
        res = []
        while i < j:
            summ = numbers[i] + numbers[j]
            if summ == target:
                res = [i + 1, j + 1]
                break
            elif summ > target:
                j -= 1
            elif summ < target:
                i += 1
        return res