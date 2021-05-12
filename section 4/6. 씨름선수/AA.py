import sys
# sys.stdin = open('input.txt', 'rt')

a=[]

n= int(input())
for _ in range(n):
  a.append(tuple(map(int, input().split())  ))

a.sort(reverse = True)

tmp = 0
cnt = 0
result = []
for x, y in a:
  # print(x, y)
  if y > tmp:
    tmp = y
    cnt += 1
    result.append((x,y))

print(cnt)
# print(result)