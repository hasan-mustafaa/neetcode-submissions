class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        #Prefix and Postfix, must start at 1 due to multiplication
        prefix = 1
        for i in range(len(nums)):
            #We multiply by prfix, before adding the current number, because otherwise it includes the current number
            #We're trying to exclude the current number
            res[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
    
            res[i] *= postfix
            postfix *= nums[i]
        
        return res