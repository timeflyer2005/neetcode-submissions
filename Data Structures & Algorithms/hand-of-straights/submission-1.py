class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for start in sorted(count):

            group = count[start]
            if group > 0 :
                for card in range(start, start + groupSize):

                    if count[card] < group:
                        return False
                    count[card] -= group
        return True