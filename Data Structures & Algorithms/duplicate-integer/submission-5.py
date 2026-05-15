class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        removed_duplicates = set(nums)
        
        return len(removed_duplicates) != len(nums)
        