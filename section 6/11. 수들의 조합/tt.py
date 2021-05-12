import sys
import itertools as it
sys.stdin=open("input.txt", "r")

n, f = (map(int, input().split())) # 5 3
a = list(map(int, input().split())) # 2 4 5 8 12
t = int(input()) # 6
print(n, f, a, t)

cnt=0

for x in it.combinations(a, f):
    if sum(x)%t==0:
        print(*x, sum(x))
        cnt+=1
print(cnt)
