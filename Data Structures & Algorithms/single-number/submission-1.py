class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        for num in nums:
            if hashMap[num] == 1:
                return num