class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        for i, char in enumerate(strs[0]):
            if any(i == len(s) or s[i] != char for s in strs):
                return strs[0][:i]

        return strs[0]
