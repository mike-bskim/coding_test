import sys
# sys.stdin=open('in1.txt', 'rt')
# input=sys.stdin.readline

def DFS(x,y):
    global cnt

    a[x][y]=0
    cnt+=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and a[xx][yy]==1:
            DFS(xx,yy)
    

if __name__ == '__main__':

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    n=int(input())
    a=[list(map(int, input())) for _ in range(n)]
    # for x in a:
    #     print(x)

    res=list()
    cnt=0
    for i in range(n):
      for j in range(n):
          if a[i][j]==1:
              cnt=0
              DFS(i, j)
              res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)