class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        res = []

        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (distance, [x, y]))
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res