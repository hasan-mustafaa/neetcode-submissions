class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        result = set(nums)

        for num in nums:
            streak = 0

            if (num - 1) not in result:
                while (num + streak) in result:
                    streak += 1
            
            max_streak = max(max_streak,streak)
        
        return max_streak

        



            


'''
Create a set
Add value to set if not in set
increment counter
'''