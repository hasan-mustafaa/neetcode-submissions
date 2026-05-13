class Solution:
        def isValid(self, s: str) -> bool:
                stack = []
                pairs = {"]":"[", ")":"(","}":"{"}
    
                for char in  s:
                    if char not in pairs:
                        stack.append(char)
                    elif stack and stack[-1] == pairs[char]:
                        stack.pop()
                    else:
                        return False
    
                if len(stack) == 0:
                    return True
                else:
                    return False
