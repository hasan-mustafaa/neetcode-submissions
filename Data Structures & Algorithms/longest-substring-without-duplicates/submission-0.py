class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = longest_sub = curr = 0
        unique_char = set()

        for right in range(len(s)):
            while s[right] in unique_char:
                curr -= 1
                unique_char.remove(s[left])
                left += 1
            

            unique_char.add(s[right])
            curr += 1
        
            if curr > longest_sub:
                longest_sub = curr
        
        return longest_sub
            

                


        



'''
Add each letter to set
If a letter is already in set, increment left pointer
If not in set, increment count
return maxCount
'''
            

        