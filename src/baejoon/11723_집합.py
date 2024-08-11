
import sys

input = sys.stdin.readline

n = int(input())
ans = set()
for _ in range(n):

    cmd = input().split()

    if len(cmd) == 2:
        cmd[1] = int(cmd[1])

    if cmd[0] == 'add':
        ans.add(int(cmd[1]))

    elif cmd[0] == "remove":
        if cmd[1] in ans:
            ans.remove(cmd[1])
    elif cmd[0] == "check":
        if cmd[1] in ans:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if cmd[1] in ans:
            ans.remove(cmd[1])
        else:
            ans.add(int(cmd[1]))
    elif cmd[0] == "all":
        ans.clear()
        for i in range(1, 21):
            ans.add(i)
    elif cmd[0] == "empty":
        ans.clear()
