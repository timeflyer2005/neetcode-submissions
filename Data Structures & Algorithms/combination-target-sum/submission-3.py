class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        subset = []

        def backtrack(index, current_sum):

            if current_sum == target:
                result.append(subset.copy())
                return
            
            if index >= len(nums) or current_sum > target:
                return
            
            subset.append(nums[index])
            backtrack(index, current_sum + nums[index])
            subset.pop()
            backtrack(index + 1, current_sum)
            
        backtrack(0,0)
        return result


            