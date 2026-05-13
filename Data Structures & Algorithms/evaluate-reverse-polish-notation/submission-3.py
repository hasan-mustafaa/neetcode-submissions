class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        operators = {"+","-","*","/"}

        for char in tokens:
            if  char not in operators:
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(a+b)
                elif char == '-':
                    stack.append(a-b)
                elif char == '*':
                    stack.append(a*b)
                elif char == '/':
                    stack.append(int(a/b))
        return stack.pop()

                    