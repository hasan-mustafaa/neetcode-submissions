class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        # l is the min value index
        # l - 1 is the max value index

        if target >= nums[l] and target <= nums[-1]:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0

        
        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
      
        




      

