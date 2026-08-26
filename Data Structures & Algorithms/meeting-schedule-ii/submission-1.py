"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key =lambda meeting: meeting.start)
        minheap = []
        maximum_rooms = 0
        for meeting in intervals:

            while minheap and minheap[0] <= meeting.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, meeting.end)
            
            maximum_rooms = max(maximum_rooms, len(minheap))
        
        return maximum_rooms
                