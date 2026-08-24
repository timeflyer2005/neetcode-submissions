class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        farthest = 0

        for i, num in enumerate(nums):

            if i > farthest:
                return False
            
            farthest = max(farthest, i + num)

            if farthest >= len(nums) - 1:
                return True
        
        return True