class Solution:
    def simplifyPath(self, path: str) -> str:

        ans = ""
        stack = []


        components = path.split('/')

        for item in components:

            if item == '..':

                if stack:
                    stack.pop()

            elif item == '.' or item == '':
                continue

            else:
                stack.append(item)

        if stack :
            ans = "/" + "/".join(stack)
        else:
            ans = "/"

        return ans

