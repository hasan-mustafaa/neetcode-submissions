import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    
        def feasible (mid):
            limit = mid
            req_days = 0

            if mid < max(weights):
                return False
            
            for weight in weights:
                limit -= weight

                if limit < 0:
                    req_days += 1
                    limit = mid
                    limit -= weight
            
            req_days += 1
            
            if req_days > days:
                return False
            else:
                return True

            


        l = 1
        r = sum(weights)
        while l < r:
            mid = (l+r) // 2

            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        