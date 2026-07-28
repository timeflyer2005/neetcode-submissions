class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        path = []

        def is_palindrome(substring):
            return substring == substring[::-1]

        def backtrack(start):
            # We successfully used every character
            if start == len(s):
                result.append(path.copy())
                return

            # Try every substring starting at `start`
            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result