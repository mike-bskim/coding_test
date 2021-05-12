import sys
sys.stdin = open('input.txt', 'rt')

n, target = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
s=0
e=n-1
mid=(s+e)//2
# print(n, target, a)
i=0
while True:
  i += 1 
  print('i: ', i)
  if target == a[mid]:
    print(mid+1)
    break
  elif target < a[mid]:
    e=mid-1
    mid = (s+e)//2
  else:
    s=mid+1
    mid = (s+e)//2


