import sys
# sys.stdin=open('in1.txt', 'rt')

def DFS(L, s):
  global res

  if L==m:
    sum=0
    for j in range(len(hs)):
      x1=hs[j][0]
      y1=hs[j][1]
      dis=2147000000
      for x in cb:
        # print(x, end=' ')
        dis= min(dis, abs(x1-pz[x][0])+abs(y1-pz[x][1]))
      sum+=dis
      # print()
    
    # print('sum:', sum)

    if sum < res:
      res=sum
      # print('cb:', cb, 'sum:', sum)

  else:
    for i in range(s, len(pz)):
      cb[L]=i
      DFS(L+1, i+1)


if __name__ == '__main__':
  n, m = map(int, input().split())
  # print(n,m)
  board=[list(map(int, input().split())) for _ in range(n)]
  # for x in board:
  #   print(x)
  hs=[]
  pz=[]
  cb=[0]*m
  # print(cb)
  res=2147000000
  for i in range(n):
    for j in range(n):
      if board[i][j]==1:
        hs.append((i,j))
      elif board[i][j]==2:
        pz.append((i,j))

  DFS(0,0)
  print(res)

