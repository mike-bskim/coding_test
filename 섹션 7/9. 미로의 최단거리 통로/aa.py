import sys
from collections import deque
# sys.stdin=open('in10.txt', 'rt')
# input=sys.stdin.readline

if __name__ == '__main__':

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    # n=int(input())
    n=7
    a=[list(map(int, input().split())) for _ in range(n)]
    dis=[[0]*n for _ in range(n)]
    # for x in ch:
    #     print(x)

    dQ=deque()
    dQ.append((0,0))

    while dQ:
        now = dQ.popleft()
        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]

            if 0<=x<n and 0<=y<n:
                if a[x][y]==0:
                    a[x][y]=1
                    dis[x][y]=dis[now[0]][now[1]]+1
                    # print(x,y, '>>>', dis[x][y])
                    dQ.append((x,y))
    if dis[n-1][n-1] == 0:
        print(-1)
    else: 
        print(dis[n-1][n-1])

