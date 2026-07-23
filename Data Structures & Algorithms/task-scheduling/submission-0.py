class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = {}

        for task in tasks:
            if task not in counts:
                counts[task] = 1
            else:
                counts[task] += 1

        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count < 0:
                    cooldown.append((count, time + n))
            if cooldown and cooldown[0][1] == time:
                count, available_time = cooldown.popleft()
                heapq.heappush(max_heap, count)

        return time