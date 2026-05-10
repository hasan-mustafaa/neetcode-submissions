class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        quick_lookup = {}

        for i, num in enumerate(nums):
            value_req = target - num
            if value_req in quick_lookup:
                if i < quick_lookup[value_req]:
                    return [i, quick_lookup[value_req]]
                else:
                    return [quick_lookup[value_req], i]
            if num not in quick_lookup:
                quick_lookup[num] = i

        
#Check if num is in array nums
# Add to set
# Iterate through array and use O(1) lookup in set


#Set only stores values not indices