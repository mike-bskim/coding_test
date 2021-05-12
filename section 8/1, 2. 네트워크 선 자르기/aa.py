import sys
# sys.stdin=open('input.txt', 'rt')

if __name__=='__main__':
  n = int(input())
  # print(n)

  a=[0]*(n+1)
  # print(a)

  a[1]=1
  a[2]=2
  for i in range(3, n+1):
    a[i] = a[i-1] + a[i-2]
    # print(i, '>>', a[i])
  print(a[n])
  