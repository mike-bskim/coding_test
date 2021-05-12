import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

# 회전 하기
for i in range(m):
  # print()
  x, y , z = (map(int, input().split()))
  # print(a[x-1])
  # print(x, y, z)
  if(y==0): # 0 이면 왼쪽 1 이면 오른쪽.
    for j in range(z):
      a[x-1].append(a[x-1].pop(0))
      # print(a[x-1])
  else:
    for j in range(z):
      a[x-1].insert(0, a[x-1].pop())
      # print(a[x-1])
s=0
e=n-1
apple = 0
for i in range(n):
  # for j in range(s,e+1):
  #   apple +=a[i][j]
  apple += sum(a[i][s:e+1])

  if(i<n//2):
    s+=1
    e-=1
  else:
    s-=1
    e+=1

print(apple)
