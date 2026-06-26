class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        size = len(s1)

        s1new = sorted(s1)

        for r in range(len(s2)):

            s2new = sorted(s2[r:r + size])

            if s1new == s2new:

                return True

        return False





