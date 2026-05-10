class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            right = len(nums) - 1
            left = i + 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return result



'''
        for i, num in enumerate(nums):
            right = len(nums) - 1
            left = i + 1
            if nums[i] == nums[i-1]: #Ensure not out of bounds
                continue
            sum = nums[right] + nums[left]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
        
'''
            




'''
Sort Array
Iterate through array
If Num is equal to the value before it, we continue
Then we use left and right pointer
If sum of left and right is too big, decrement right pointer
If sum of left and right is too small, increment left pointer


'''