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
                coins = nums[left] * nums[i] * nums[right]
                coins += dfs(left, i)
                coins += dfs(i, right)
                
                best = max(best, coins)

            dp[(left, right)] = best
            return best

        return dfs(0, len(nums) - 1)