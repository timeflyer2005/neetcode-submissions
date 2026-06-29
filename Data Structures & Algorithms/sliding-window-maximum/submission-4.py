class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        left = 0
        result = []

        for right in range(n):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            
            q.append(right)

            while q[0] < left:
                q.popleft()

            if right >= k - 1:
                result.append(nums[q[0]])
                left += 1
        
        return result