class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1
        mVol = 0
        while i < j:
            vol = (j - i) * min(heights[i], heights[j])
            mVol = max(vol, mVol)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return mVol