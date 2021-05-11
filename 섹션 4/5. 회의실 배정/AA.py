import sys
# sys.stdin = open('input.txt', 'rt')
a=[]
n= int(input())
for _ in range(n):
  a.append(list(map(int, input().split())  ))

a.sort(key=lambda x: (x[1], x[0]))
# print(n, a[0])
# for x in a:
#   print(x)

end = 0
cnt = 0
for s, e in a:
  if s >= end:
    end = e
    cnt += 1

print(cnt)