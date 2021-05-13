import sys
# sys.stdin=open('input.txt', 'rt')

if __name__=='__main__':
  n=int(input())
  a=[list(map(int, input().split())) for _ in range(n)]
  a.sort(reverse=True)
  # for x in a:
  #   print(x)

  res=[0]*n
  res[0]=a[0][1]
  # print(res)
  for i in range(1, n):
    # print(a[i][2], '>>>', end=' ')
    max1=0
    for j in range(i-1, -1, -1):
      # print(a[j][2], end=' ')
      if (a[i][2]<a[j][2]) and (max1<res[j]):
        max1=res[j] # me + compare
        # print('***', a[i][2], a[j][2], max1+a[i][1])
    # print()
    res[i]=max1+a[i][1]
  # print(res)
  print(max(res))
