from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = Counter(s)
        freq2 = Counter(t)

        freq1 = dict(sorted(freq1.items()))
        freq2 = dict(sorted(freq2.items()))

        if freq1 == freq2:
            return True
        else:
            return False

   