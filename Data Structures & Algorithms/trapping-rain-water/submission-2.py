class Solution:
    def trap(self, height: List[int]) -> int:
        # storing next greatest in both ltr and rtl way
        ltr= []
        rtl = []
        _max = height[0]
        for i in height:
            _max = max(i, _max)
            ltr.append(_max)
        
        _max = height[-1]

        for i in range(len(height) - 1, -1, -1):
            _max = max(_max, height[i])
            rtl.append(_max)

        rtl.reverse()

        total_water = 0

        for i in range(0, len(height)):
            total_water += min(ltr[i], rtl[i]) - height[i]

        return total_water