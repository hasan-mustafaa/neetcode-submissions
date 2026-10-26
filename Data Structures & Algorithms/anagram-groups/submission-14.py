
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = defaultdict(list)

        for s in strs:
            key = frozenset(Counter(s).items())
            sublists[key].append(s)
        
        return list(sublists.values())