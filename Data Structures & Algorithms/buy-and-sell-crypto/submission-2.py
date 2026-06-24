class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_p = max(max_p, prices[j] - prices[i])
        return max_p