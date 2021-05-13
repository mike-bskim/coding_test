import sys
# sys.stdin=open('in2.txt','rt')

if __name__=='__main__':
  n = int(input())
  R=list(map(int, input().split()))
  L=[0 for i in range(n)]

  # for i in range(n):
  # print(L)
  # print(R)
  # print()

  L[0]=1
  for i in range(1, n):
    max1=0
    for j in range(i-1, -1, -1):
      # print(R[i], R[j])
      if(R[i]>R[j]) and L[j]>=max1:
        max1 = L[j]
        # print('>>> R[{}]:{}, R[{}]:{}, max1:{}, L:{}'.format(i, R[i], j, R[j], max1+1, L))
    L[i]=max1+1
  # print('last:',L)
  print(max(L))



