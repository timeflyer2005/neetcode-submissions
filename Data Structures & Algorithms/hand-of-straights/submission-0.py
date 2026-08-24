class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for start in sorted(count):
            groups = count[start]

            if groups > 0:
                for card in range(start, start + groupSize):
                    if count[card] < groups:
                        return False
                    
                    count[card] -= groups
        
        return True 
        
