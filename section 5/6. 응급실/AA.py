import sys
from collections import deque
# sys.stdin = open('in3.txt', 'rt')

# n = int(input())
n, m = map(int, input().split())
a = [ (pos, val) for pos, val in enumerate(list(map(int, input().split())))]
a = deque(a)
# print(n, m, a)

cnt = 0
while True:
  x = a.popleft()
  if x[1] < max(a, key=lambda x:x[1])[1]:
    a.append(x)
  else:
    # print('x[1] max : ', x, max(a, key=lambda x:x[1]))
    cnt += 1
    if x[0] == m:
      print(cnt)
      break
