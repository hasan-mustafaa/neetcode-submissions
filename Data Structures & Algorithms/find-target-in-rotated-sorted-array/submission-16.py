class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            M = (L + R) // 2

            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M


        min_index = L

        if min_index == 0: #Not rotated, regular binary search case
            l = 0
            r = len(nums) - 1
        elif target >= nums[0] and target <= nums[min_index - 1]: # Left Half
            l = 0
            r = min_index - 1
        else: #Right Half
            l = min_index 
            r = len(nums) - 1
        
        #Regular binary search
        while l <= r:
            m = (l+r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
        
        return -1

