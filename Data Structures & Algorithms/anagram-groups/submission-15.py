from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            freq_map = frozenset(Counter(s).items())
            groups[freq_map].append(s)
        
        return list(groups.values())