class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append((str(len(s)) + "#" + s))

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        left, right = 0, 0
        res = []

        while right < len(s):
            left = right

            while s[right] != "#":
                right += 1
        
            w_length = int(s[left: right])
            left = right + 1
            right = left + w_length
            res.append(s[left: right])

        return res



"""

5#Hello


"""