class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def feasible(candidate):
            num_days = 1
            limit = candidate

            for weight in weights:
                limit -= weight
                if limit < 0:
                    limit = candidate
                    limit -= weight
                    num_days += 1

            return num_days <= days
        

        while l < r:
            mid = (l + r) // 2

            if feasible(mid):
                r = mid
            else:
                l = mid + 1  

        return l

"""
Trace: weights = [2,4,6,1,3,10], days = 4
5 - 2 = 3
3 - 4 = -1, 1
5 - 6 = - 1, 2
5 - 1 = 4
4 - 3, 





"""

            