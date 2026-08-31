class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        #Has to start by one, else r -1 is out of bounds, and 1st element is always unique
        for r in range(1, len(nums)): 
            if nums[r] != nums[r - 1]: #If consecutives numbers are not equal, then it's a unique number
                nums[l] = nums[r]
                l += 1
        return l



        