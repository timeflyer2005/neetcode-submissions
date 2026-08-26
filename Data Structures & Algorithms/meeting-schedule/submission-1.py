class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda interval: interval.start)
        previous_end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start < previous_end:
                return False

            previous_end = interval.end

        return True