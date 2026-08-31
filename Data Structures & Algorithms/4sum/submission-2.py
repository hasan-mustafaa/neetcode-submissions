class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Exactly the same as 3 sum, but with 1 extra loop and dedup logic, and second loop starts from
        index after first loop, alongside in the dedup logic
        """

        nums.sort()
        res = []

        for k in range(len(nums) -1):

            if k > 0 and nums[k] == nums[k-1]:
                    continue

            for i in range(k + 1, len(nums) - 1):

                if i > k + 1 and nums[i] == nums[i-1]:
                    continue
                
                l = i + 1
                r = len(nums) - 1

                while l < r:
                    num_sum = nums[k] + nums[i] + nums[l] + nums[r]

                    if num_sum == target:
                        res.append([nums[k], nums[i], nums[l], nums[r]])
                        l, r = l + 1, r - 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif num_sum < target:
                        l += 1
                    else:
                        r -= 1
                
        return res
                    

        