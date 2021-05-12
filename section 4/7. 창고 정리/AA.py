import sys
# sys.stdin = open('input.txt', 'rt')

a=[]

n= int(input())
a = list(map(int, input().split()))
chance = int(input())
# print(n, a, chance)

gap = 0
for i in range(chance):
  a.sort()
  a[0]+=1
  a[n-1]-=1

a.sort()
print(a[n-1]-a[0])
