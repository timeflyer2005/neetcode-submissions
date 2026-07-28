class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        path = []

        def palindrome(left, right):

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        def backtrack(start):

            if start == len(s):
                result.append(path.copy())
            
            for end in range(start, len(s)):
                if palindrome(start, end):
                    path.append(s[start: end + 1])
                    backtrack(end + 1)
                    path.pop()
        backtrack(0)
        return result   

