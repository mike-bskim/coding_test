import sys
# sys.stdin = open('input.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# print(n, a)

apple = 0

# print(sum(a[0][2:3]))
# print(sum(a[1][1:4]))
# print(sum(a[2][0:5]))
# print(sum(a[3][1:4]))
# print(sum(a[4][2:3]))
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
      apple += a[i][j]
    #   print(i, s, e)
    if(i < n//2):
      s -= 1
      e += 1
    else:
      s += 1
      e -= 1

print(apple)    
