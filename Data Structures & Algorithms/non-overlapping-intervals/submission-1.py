class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        previous_end = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:
            if start >= previous_end:
                previous_end = end
            else:
                count += 1
                previous_end = min(end, previous_end)
        return count