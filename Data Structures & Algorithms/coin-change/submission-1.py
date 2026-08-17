class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}

        def dfs(amount):

            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in dp:
                return dp[amount]
            
            res = float("inf")

            for coin in coins:
                res = min(res, 1 + dfs(amount - coin))

            dp[amount] = res
            return res

        ans = dfs(amount)
        if ans == float("inf"):
            return -1
        
        return ans