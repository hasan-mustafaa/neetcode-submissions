class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            dif = target - num
            if dif in seen:
                return [seen[dif], index]
            seen[num] = index
        
            