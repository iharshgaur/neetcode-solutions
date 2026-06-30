class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0;
        j = len(heights) - 1
        maxVol = 0
        while ( i < j ):
            area = min(heights[i], heights[j]) * (j - i)
            maxVol = max(area, maxVol)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maxVol