class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMax = nums[0]
        curMin = nums[0]
        maxProduct = nums[0]

        for num in nums[1:]:
            newMax = max(num, curMax * num, curMin * num)
            newMin = min(num, curMin * num, curMax * num)

            curMax = newMax
            curMin = newMin

            maxProduct = max(maxProduct, curMax)
        
        return maxProduct
