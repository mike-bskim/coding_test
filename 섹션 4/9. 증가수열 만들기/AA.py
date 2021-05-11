import sys
# from collections import deque
# sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
# print(n, a)
s=0
e=n-1
result=''
tmp =[]
max1 = 0

while s<=e:
  # print('position: ', s,e)
  if a[s] > max1:
    tmp.append((a[s], 'L'))
  if a[e] > max1:
    tmp.append((a[e], 'R'))
  tmp.sort()

  if len(tmp) == 0:
    break
  else:
    max1 = tmp[0][0]
    result += tmp[0][1]

    if tmp[0][1] == 'L':
      # print(a[s])
      s +=1
    else:
      # print(a[e])
      e -=1
  tmp.clear()

print(len(result))
print((result))