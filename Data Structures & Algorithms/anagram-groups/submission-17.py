from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1

            #Keys must be hashable, so tuple, frozenset 
            groups[tuple(count)].append(s)
    
        return list(groups.values())
        
