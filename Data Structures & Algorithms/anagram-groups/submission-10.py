
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            freq = Counter(word)
            key = tuple(sorted(freq.items()))
            groups[key].append(word)
        
        return list(groups.values())

        