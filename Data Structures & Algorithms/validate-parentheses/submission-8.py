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


        """
        1. Basically build stack of opening brackets
        2. After building, iterate over the closing ones, and return False if they don't match top value on stack, and pop
        3. Repeat


        Note: Return True, only if stack is empty once loop is over, meaning that all matches have been completed
        """