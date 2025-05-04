
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        op = {'+', '-', '*', '/'}

        for tk in tokens:
            if tk not in op:
                stack.append(int(tk))
                continue

            b = stack.pop()
            a = stack.pop()

            if tk == '+':
                stack.append(a+b)
            elif tk == '-':
                stack.append(a-b)
            elif tk == '*':
                stack.append(a*b)
            else:
                stack.append(int(a/b))

        return stack[0]


if __name__ == "__main__":

    tokens = ["2", "1", "+", "3", "*"]

    sol = Solution()
    print(sol.evalRPN(tokens))