class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        index = 0
        for num in nums:
            for n in range (0,index):
                if n == index:
                    continue
                result[index] *= nums[n]
            for n in range (index + 1, len(nums)):
                if n == index:
                    continue
                result[index] *= nums[n]
            index += 1
        
        return result