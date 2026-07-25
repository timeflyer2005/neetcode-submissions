class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        subset = []

        def backtrack(index):

            if index == len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            
            backtrack(index + 1)
        
        backtrack(0)
        return result 




                

            