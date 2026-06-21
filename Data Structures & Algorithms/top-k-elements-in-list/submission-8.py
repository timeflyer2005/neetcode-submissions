class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        array = []

        for val, cnt in count.items():
            array.append([cnt, val])
        array.sort()

        res = []

        while len(res) < k:
            res.append(array.pop()[1])
        
        return res

        
            
        