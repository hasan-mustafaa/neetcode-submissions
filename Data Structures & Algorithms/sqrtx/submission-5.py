class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0

        while l <= r:
            mid = (r+l) // 2

            if mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
                ans = mid
            else:
                return mid
        
        return ans
        
