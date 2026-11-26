class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #2 Pointers only works when sorted dataset
        nums.sort()

        for i in range(len(nums)):
            
            #We need to have this while loop, to avoid picking duplicates
            #We have the i>0 to prevent the first loop to be referencing the last element in the array
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    #We need to have this while loop, to avoid picking duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res

"""
Problem is quite standard, except the fact that to avoid duplicates
1. You sort
2. Since duplicates are next to each other, you check if they are next to check other and skipw
"""

        
    