class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        signs=['+', '-', '*','/']
        for i in tokens:
            if i.isdigit() or (len(i) > 1 and i[0] == '-' and i[1:].isdigit()):
                stack.append(int(i))
            elif i in signs:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                else:   # '/'
                    # truncate toward 0
                    stack.append(int(a / b))
        return stack[-1]
                


        