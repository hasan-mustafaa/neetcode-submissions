class Solution:
        def isValid(self, s: str) -> bool:
            stack = []
            brackets = {']':'[', '}':'{', ')':'('}

            for char in s:
                if char in brackets.values():
                    stack.append(char)
                elif char in brackets:
                    if not stack or stack[-1] != brackets[char]:
                        return False
                    stack.pop()
            return not stack                

