import sys
# sys.stdin=open('in4.txt','rt')
# input=sys.stdin.readline
sys.setrecursionlimit(3*10**6)
# print(sys.getrecursionlimit())

def DFS(x,y,T):
  global cnt_debug

  cnt_debug+=1
  ch[x][y]=1

  for i in range(4):
    xx=x+dx[i]
    yy=y+dy[i]

    if 0<=xx<n and 0<=yy<n and a[xx][yy]>T:
      if ch[xx][yy]==0:
        # print('>>>cnt:', cnt_debug, end=' ')
        DFS(xx,yy,T)

if __name__=='__main__':
  dx=[-1,0,1,0]
  dy=[0,1,0,-1]
  n=int(input())
  a=[list(map(int, input().split())) for _ in range(n)]

  max1=0
  for xx in a:
    for x in xx:
      if x>max1:
        max1=x
  
  res=list()
  for t in range(1, 100):
    if t > max1:
      break
    cnt=0
    ch=[[0]*n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        if a[i][j]>t and ch[i][j]==0:
          # print('for', i,j,t)
          cnt_debug=0
          DFS(i,j,t)
          # print('cnt_debug:', cnt_debug)
          cnt+=1
    res.append(cnt)
  print(max(res))
    


