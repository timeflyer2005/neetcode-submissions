class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            value = abs(nums[i])
            index = value - 1

            if nums[index] < 0:

                return value

            nums[index] *= -1
            