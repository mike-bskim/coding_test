import sys
from collections import deque
# sys.stdin = open('input.txt', 'rt')
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n, m = map(int, input().split())
# print(n, m)

board=[list(map(int, input().split())) for _ in range(m)]
dis=[[0]*n for _ in range(m)]
Q=deque()
max1=0
for i in range(m):
  for j in range(n):
    if board[i][j]==1:
      Q.append((i,j))

while Q:
  tmp=Q.popleft()
  for i in range(4):
    xx = tmp[0]+dx[i]
    yy = tmp[1]+dy[i]

    if(0<=xx<m) and (0<=yy<n) and board[xx][yy]==0:
      board[xx][yy]=1
      dis[xx][yy]=dis[tmp[0]][tmp[1]] + 1
      Q.append((xx,yy))
      max1=dis[xx][yy]

for i in range(m):
  for j in range(n):
    if board[i][j]==0:
      max1=-1

print(max1)
