class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def rec(i,j):
            if i<0 or j<0:
                return 0 
            elif dp[i][j] != -1:
                return dp[i][j]
            elif text1[i] == text2[j]:
                dp[i][j] = 1 + rec(i-1,j-1)
                return dp[i][j]
            else :
                dp[i][j] = max(rec(i-1,j) , rec(i,j-1))
                return dp[i][j]

        n = len(text1)
        m = len(text2)
        dp = [[-1] * m for _ in range(n)]

        return rec(n-1,m-1)