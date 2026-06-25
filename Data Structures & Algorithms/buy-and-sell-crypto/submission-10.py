class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) <= 1:
            return res
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            else:
                profit = prices[r] - prices[l]
                res = max(profit,res)
                r += 1
        return res