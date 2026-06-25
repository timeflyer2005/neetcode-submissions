class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        window = Counter(s2[:len(s1)])

        for i in range(len(s2) - len(s1)):
            if window == s1Count:
                return True
            
            # Slide the window
            char_to_remove = s2[i]
            char_to_add = s2[i + len(s1)]
            
            window[char_to_remove] -= 1
            if window[char_to_remove] == 0:
                del window[char_to_remove]
            window[char_to_add] += 1
            
        return window == s1Count