class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(queries)

        answers = {}
        heap = []
        interval_index = 0

        for query in sorted_queries:
            # Add every interval that starts before or at query
            while (
                interval_index < len(intervals)
                and intervals[interval_index][0] <= query
            ):
                left, right = intervals[interval_index]
                length = right - left + 1

                heapq.heappush(heap, (length, right))
                interval_index += 1

            # Remove intervals that end before query
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            # The shortest valid interval is at the top
            if heap:
                answers[query] = heap[0][0]
            else:
                answers[query] = -1

        # Restore the queries' original order
        return [answers[query] for query in queries]