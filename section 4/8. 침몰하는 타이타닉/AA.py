import sys
from collections import deque
# sys.stdin = open('input.txt', 'rt')

n, w= map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
# print(n,w, a)

cnt = 0

while a:
  if(len(a) == 1):
    cnt += 1
    break

  if a[0]+a[-1] > w:
    b = a.pop()
    # print('>>>',b)
    cnt += 1
  else:
    b=a.pop()
    # print(b)
    b=a.popleft()
    # print(b)
    cnt += 1
print(cnt)
