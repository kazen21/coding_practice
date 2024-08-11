
from collections import defaultdict
n, m = map(int, input().split())
# print(n,m)
dic = defaultdict(int)
# a = ["ohhenrie", "charlie", "baesangwook"]
# b = ["obama", "baesangwook", "ohhenrie", "clinton"]
for _ in range(n):
    name = input()

    dic[name] += 1

for _ in range(m):
    name = input()
    dic[name] += 1

# print(dic)
ans = []
for k, v in dic.items():
    if v == 2:
        ans.append(k)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])


