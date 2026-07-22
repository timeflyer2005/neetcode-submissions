class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        

        while len(max_heap) > 1:
            stone1 = -1 * heapq.heappop(max_heap)
            stone2 = -1 * heapq.heappop(max_heap)
            
            if stone2 != stone1:
                heapq.heappush(max_heap, -(stone1 - stone2))
        
        return -1 * max_heap[0] if max_heap else 0



            