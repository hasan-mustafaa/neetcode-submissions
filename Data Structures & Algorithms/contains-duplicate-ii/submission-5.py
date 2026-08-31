class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        curr_win = set()
        flag = False

        for right in range(0, len(nums)):
            if nums[right] in curr_win:
                flag = True
                return flag
            curr_win.add(nums[right])

            if len(curr_win) > k:
                curr_win.discard(nums[right-k])
        

        return flag


        
