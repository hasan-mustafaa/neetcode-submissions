import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "/", "*"}
        
        for token in tokens:

            if token in operators:
                
                #Need to define variables, math evaluated from left to right
                val1 = stack.pop()
                val2 = stack.pop()

                if token == "+":
                    stack.append(val2 + val1)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val2 * val1)
                elif token == "/":
                    # math.floor and // both round to negative infinity
                    # Use int to truncate
                    stack.append(int(val2 / val1))
            else:
                stack.append(int(token))
    
        return stack[-1]

