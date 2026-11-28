import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Binary Search over the search space
        l, r = 1, max(piles)

        def feasible(candidate):
            count = 0

            for pile in piles:
                count += math.ceil(pile/candidate)

            return count <= h

        

        while l < r:
            mid = (r + l) // 2

            if feasible(mid):
                r = mid
            else:
                l = mid + 1

        return l
    

    """
    Space: O(1)
    Time: O(n log M)

    Trace: piles = [1,4,3,2], h = 9
    Candidate: 2, (1, 2, 2, 1) = 6 hours
    Candidate: 1: (1, 4, 3, 2) = 10 hours
    Hence smallest valid candidate is 2

    """