import sys
# sys.stdin = open('in1.txt', 'rt')

n, m = list(map(int, input().split()))

tmp = [0] * (n+m+1)
# print(tmp)

for a in range(1, n+1):
  for b in range(1, m+1):
    c = a + b
    tmp[c] += 1
    # print(a, b, c)

max_num = max(tmp)
# print(tmp)
# for i in range(len(tmp)):
#   if(tmp[i] == max_num):
#     print(i, end=' ')

for idx, val in enumerate(tmp):
  if(val == max_num):
    print(idx, end=' ')

