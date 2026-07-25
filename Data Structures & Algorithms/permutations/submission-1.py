class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        subset = []

        def backtrack():

            if len(subset) == len(nums):
                result.append(subset.copy())
                return
            
            for num in nums:
                if num in subset:
                    continue

                subset.append(num)
                backtrack()
                subset.pop() 
            
        backtrack()
        return result