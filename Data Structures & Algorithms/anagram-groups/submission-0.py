class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
    
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            
            result[tuple(freq)].append(string)

        return list(result.values())
       
       

                


# O(nm) complexity, hence nested loops
# Loop through every string in strs
# Create an empty list
# Check if it's an anagram with every other string
# Append all strings to it, and remove from strs
# Repeat