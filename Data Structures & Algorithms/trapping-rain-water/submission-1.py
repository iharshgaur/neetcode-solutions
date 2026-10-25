class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        current_max = height[0]
        for i in range(n):
            current_max = max(current_max, height[i])
            left_max[i] = current_max
        
        current_max = height[n-1]
        for i in range(n-1, -1, -1):
            current_max = max(current_max, height[i])
            right_max[i] = current_max

        total = 0
        for i in range(n):
            total += min(left_max[i], right_max[i]) - height[i]
        return total