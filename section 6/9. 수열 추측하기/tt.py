import sys
import itertools as it
sys.stdin=open("input.txt", "r")

n, f=map(int, input().split())
b=[1]*n
cnt=0
for i in range(1,n):
    b[i]=b[i-1]*(n-i)//i
a=list(range(1, n+1))

print(n, f, a, b)

# 순열만들어주는 라이브러리.
for tmp in it.permutations(a):
    sum=0
    for L, x in enumerate(tmp):
        sum+=x*b[L]
    if sum % f == 0:
        print(*tmp)
        cnt+=1
        break
# print(cnt)

# for x in it.combinations(a, k):
#     if sum(x)%m==0:
#         cnt+=1
# print(cnt)
