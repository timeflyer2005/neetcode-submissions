class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for i in range(len(s)):
            res = set()
            length = 0
            for j in range(i, len(s)):
                if s[j] in res:
                    break
                else:
                    res.add(s[j])
                    length += 1
            if length > max_length:
                max_length = length
        return max_length