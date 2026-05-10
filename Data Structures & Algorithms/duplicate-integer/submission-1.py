class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDuplicates = set()
        for value in nums:
            if value in checkDuplicates:
                return True
            checkDuplicates.add(value)
        return False
        

#Check if each element is in the hashset
# Add each element to a hashset
# If there is a math return true else return false