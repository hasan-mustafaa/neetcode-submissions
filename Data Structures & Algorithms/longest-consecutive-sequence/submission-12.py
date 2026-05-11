class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        sorted_nums = sorted(unique_nums)
        l_seq = 0
        seq = 1

        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        for i, num in enumerate(sorted_nums[:-1]):
            if sorted_nums[i] + 1 == sorted_nums[i+1]:
                seq += 1
                l_seq = max(l_seq, seq)
                continue
            seq = 1
        
        l_seq = max(l_seq, seq)
        return l_seq    
            
