class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_stored = 0

        while l < r:
            stored_water = min(heights[l], heights[r]) * (r - l)
            max_stored = max(max_stored, stored_water)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_stored
        