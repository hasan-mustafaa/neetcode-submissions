class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,value in enumerate(nums):
            dif = target - value
            if dif in seen:
                return [seen[dif], index]
            seen[value] = index