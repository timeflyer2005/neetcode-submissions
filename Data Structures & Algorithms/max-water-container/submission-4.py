class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] > heights[r]:
                curr = heights[r] * (r - l)
                r -= 1
            elif heights[l] < heights[r]:
                curr = heights[l] * (r - l)
                l += 1
            else:
                curr = heights[l] * (r - l)
                l += 1

            if curr > largest:
                largest = curr
        return  largest

