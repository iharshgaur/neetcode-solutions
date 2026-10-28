class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (earliest start index, height)
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                left, old_height = stack.pop()

                max_area = max(max_area, old_height * (i - left))
                start = left

            stack.append((start, height))

        for left, height in stack:
            max_area = max(max_area, height * (len(heights) - left))

        return max_area