class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        curr_sum = 0
       

        def backtrack(i):
            nonlocal curr
            nonlocal curr_sum

            if curr_sum == target:
                res.append(curr[:])
                return
            
            if curr_sum > target or i >= len(nums):
                return

            curr_sum += nums[i]
            curr.append(nums[i])
            backtrack(i)
            curr.pop()
            curr_sum -= nums[i]

            backtrack(i + 1)

        
        backtrack(0)
        return res
            

            
            
