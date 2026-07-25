class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        subset = []

        def backtrack(opens, closes):

            if opens == n and closes == n:
                result.append("".join(subset))
                return

            if opens < n:
                subset.append("(")
                backtrack(opens + 1, closes)
                subset.pop()
            
            if closes < opens:
                subset.append(")")
                backtrack(opens, closes + 1)
                subset.pop()
            
        backtrack(0,0)
        return result