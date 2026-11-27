class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        win_sum = 0
        min_win_length = float("inf")

        for right in range(len(nums)):

            win_sum += nums[right]

            while win_sum >= target:
                min_win_length = min(min_win_length, right - left + 1)
                win_sum -= nums[left]
                left += 1
            

        return min_win_length if min_win_length != float("inf") else 0
