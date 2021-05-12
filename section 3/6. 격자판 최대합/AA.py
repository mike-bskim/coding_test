import sys
# sys.stdin = open('in1.txt', 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# print(n, a)

max_num = 0

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if max_num < sum1:
        max_num = sum1
    if max_num < sum2:
        max_num = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if max_num < sum1:
    max_num = sum1
if max_num < sum2:
    max_num = sum2

print(max_num)