class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        for l in range(len(nums) - k + 1):

            window = nums[l : l + k]

            res.append(max(window))

        return res
