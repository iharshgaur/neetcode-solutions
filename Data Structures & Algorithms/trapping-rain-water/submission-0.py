class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # 1. Left Max array bharo
        # (left_max[i] ka matlab hai 0 se i tak ka sabse uncha bar)
        curr_max = 0
        for i in range(n):
            curr_max = max(height[i], curr_max)
            left_max[i] = curr_max
        
        # 2. Right Max array bharo
        # (right_max[i] ka matlab hai n-1 se i tak ka sabse uncha bar)
        curr_max = 0
        for i in range(n - 1, -1, -1):
            curr_max = max(height[i], curr_max)
            right_max[i] = curr_max
        
        # 3. Total water calculate karo
        total_water = 0
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]
            
        return total_water