import sys
# sys.stdin = open('input.txt', 'rt')

n, val = map(int, input().split())
a = list(map(int, input().split()))

# print(m, n, a)

# for i in range(m):
#     c=0
#     for j in range(i, m):
#         c += a[j]
#         # print(c, n)
#         if c == n:
#             result += 1
#             # print('match: ', i, j)
#             break
#         elif c > n:
#             # print('over: ', i, j)
#             break
# print(result)        

lt = 0
rt = 1
cnt = 0
tot = a[0]
while True:
    if tot< val:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot == val:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)