import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')

# n = int(input())
n, m = map(int, input().split())
# print(n, m)

res=list(range(1,n+1))
# print(res)

while len(res) > 1:
  for i in range(m):
    if i == (m-1):
      res.pop(0)
    else:
      res.append(res.pop(0))
print(*res)


res=list(range(1,n+1))
res=deque(res)
# print(res)

while len(res) > 1:
  res.rotate(1-m)
  x = res.popleft()
  # print('>>', x)
print(*res)



