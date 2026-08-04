class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            start = minH[0]
            for i in range(start, start+groupSize):
                if not count[i]:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if not minH[0] == i:
                        return False
                    heapq.heappop(minH)
                
        return True