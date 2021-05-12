import sys
sys.stdin=open('in3.txt', 'rt')

def DFS(L):

  # if a[L]>0:
  #   return a[L]

  if L==1 or L==2:
    # a[L]=L
    return L
    # print(cnt)
  else:
    # print('>>>', L)
    a[L]=DFS(L-1)+DFS(L-2)
    # print('***a[{}] >> {}'.format(L, a[L]))
    return a[L]

  

if __name__=='__main__':
  n = int(input())
  cnt = 0
  # print(n)

  a=[0]*(n+1)
  # print(a)
  cnt = DFS(n)
  print(cnt)

  