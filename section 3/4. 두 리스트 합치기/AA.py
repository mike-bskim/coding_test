import sys
# sys.stdin = open('input.txt', 'rt')

m = int(input())
a = list(map(int, input().split()))

n = int(input())
b = list(map(int, input().split()))
# print(m, a)
# print(n, b)

a1=0
b1=0
c=[]

while a1<len(a) and b1<len(b):
    if(a[a1]<=b[b1]):
        c.append(a[a1])
        a1+=1
    else:
        c.append(b[b1])
        b1+=1
if (a1 < len(a)):
    c = c + a[a1:]
else:
    c = c + b[b1:]    

print(*c)    