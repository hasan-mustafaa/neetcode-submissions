class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(str(len(s)) + "#" + s)
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        res = []
        left = 0

        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            w_length = int(s[left:right])
            left = right + 1
            right = left + w_length
            res.append(s[left:right])
            left = right
        
        return res


