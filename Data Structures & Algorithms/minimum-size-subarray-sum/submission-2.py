class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_win = 0
        min_len = float('inf')
        flag = False
 

        for right in range(len(nums)):
            curr_win += nums[right]
    
            while curr_win >= target:
                flag = True
                curr_len = right - left + 1
                min_len = min(min_len, curr_len)

                curr_win -= nums[left]
                left += 1
                
            
        
        if flag == False:
            return 0
        else:
            return min_len
        



            

        