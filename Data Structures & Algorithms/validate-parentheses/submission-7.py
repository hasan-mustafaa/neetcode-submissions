class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']': '['}

        for bracket in s:
            #Wait till we get to the closing brackets
            if bracket in pairs:
                if not stack or stack[-1] != pairs[bracket]:
                    return False
                stack.pop()
            else:
                #It's an opening bracket
                stack.append(bracket)

        return True if not stack else False