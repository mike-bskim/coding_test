import sys
# sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline

def DFS(x,y):

  a[x][y]=0
  # print(x,y,'>>>',a[x][y])

  for i in range(8):
    xx=x+dx[i]
    yy=y+dy[i]
    if 0<=xx<n and 0<=yy<n and a[xx][yy]==1:
      DFS(xx,yy)



if __name__=='__main__':
  dx=[-1, -1, 0, 1,1,1,0,-1]
  dy=[0,1,1,1,0,-1,-1,-1]
  n=int(input())
  a=[list(map(int, input().split())) for _ in range(n)]
  # for x in a:
  #   print(x)
  cnt=0
  for i in range(n):
    for j in range(n):
      if a[i][j] == 1:
        
        DFS(i,j)
        cnt+=1
        # print('------------')
  print(cnt)