class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_streak = 0


        for num in num_set:
            if num - 1 not in num_set:
                curr_streak = 1
                max_streak = max(curr_streak, max_streak)
                while num + 1 in num_set:
                    curr_streak += 1
                    max_streak = max(curr_streak, max_streak)
                    num += 1
        

        return max_streak


