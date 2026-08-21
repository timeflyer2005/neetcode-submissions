class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}


        def dfs(left, right):

            if left + 1 == right:
                return 0
            
            if (left, right) in dp:
                return dp[(left, right)]
            
            best = 0

            for i in range(left + 1, right):
                
                coin = nums[left] * nums[i] * nums[right]
                coin += dfs(left, i)
                coin += dfs(i, right)
                best = max(best, coin)
            

            dp[(left, right)] = best

            return best 
        return dfs(0, len(nums) - 1)
        