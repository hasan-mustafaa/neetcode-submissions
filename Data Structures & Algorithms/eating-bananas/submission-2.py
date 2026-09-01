import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def feasible(mid):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid)
            
            if total_hours <= h:
                return True
            else:
                return False


        while l < r:
            mid = (r + l) // 2

            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l


        """
        1. Validate search space, minmum eating speed is 1, maximum is the sum of the array, because if 
            h equals len of the array, then it's possible 
        """










    """
    2. Return k
    """
    