class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_num = sum(nums)

        if sum_num % 2 == 1:
            return False 
        #We can only have ints, no floats so must be even
        target = sum(nums) // 2
        sums = {0}

        for num in nums: 
            sums.update({s + num for s in sums})
            if target in sums:
                return True
        
        return False


#For every num, add to set if we pick or no pick
# if target comes up twice, return

#Pick/nopick -> binary choice