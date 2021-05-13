import sys
# sys.stdin=open('in5.txt','rt')


def DFS(L,n):
  
  if (L>n):
    return

  max1=0
  me=a[L]
  for i in range(L, 0, -1):
    if(a[i]<me) and (res[i]>max1):
      max1=res[i]
  res[L]=max1+1
  DFS(L+1, n)
    


def DFS():

  for i in range(2, n+1):
    max1=0
    for j in range(i-1, 0, -1):
      if (a[j]<a[i]) and (res[j]>max1):
        max1=res[j]
        # print('max1:{}, a[j]:{} a[i]:{} '.format(max1, a[j], a[i]))
    res[i]=max1+1

    # print('>>>a[{}]: {} max:{}'.format(i, a[i], res[i]))
    
  

if __name__=='__main__':
  n = int(input())
  a = list(map(int, input().split()))
  a.insert(0,0)
  # print(a)
  res=[0]*(n+1)
  # print(res)

  res[1]=1
  DFS()
  # print()
  # print(res, n)
  print(max(res))
