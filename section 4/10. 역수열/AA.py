import sys
# from collections import deque
# sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
# print(n, a)

r = [0]*n
cnt = 0

for i in range(n):
  for j in range(n):
    if r[j] == 0 :#and r[j] < i+1:
      cnt += 1
      # print(r[j], a[i], cnt)
      # print(i, r)
      if cnt > a[i]:
        r[j] = i+1
        cnt = 0
        # print('>>>',cnt, a[i], i+1, r)
        break
print(*r)


