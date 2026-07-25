class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        subset = []

        def backtrack(open, close):

            if len(subset) == 2 * n:
                result.append("".join(subset))
                return
            
            if open < n:
                subset.append("(")
                backtrack(open + 1, close)
                subset.pop()
            
            if close < open:
                subset.append(")")
                backtrack(open, close + 1)
                subset.pop()
        
        backtrack(0,0)
        return result
