class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            if heights[l] >= heights[r]:
                r -= 1
            else: 
                l += 1
            
            if curr > largest:
                largest = curr
        return largest
