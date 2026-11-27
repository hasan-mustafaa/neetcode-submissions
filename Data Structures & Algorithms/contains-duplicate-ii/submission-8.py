from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n_map = defaultdict(int)
        
        for i, num in enumerate(nums):

            if num in n_map:
                if abs(i - n_map[num]) <= k:
                    return True
            
            n_map[num] = i
        

        return False
            

            

            
        