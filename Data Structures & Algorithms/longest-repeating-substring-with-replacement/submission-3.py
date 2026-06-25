class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            counts, maxf = {}, 0
            for j in range(i, len(s)):
                counts[s[j]] = 1 + counts.get(s[j], 0)
                maxf = max(maxf, counts[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res
