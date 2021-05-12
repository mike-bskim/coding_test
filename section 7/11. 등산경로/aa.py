import sys
# sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline

def DFS(x,y):
    global cnt
    
    if x==ex and y==ey:
        cnt+=1

    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and a[xx][yy]>a[x][y]:
                DFS(xx,yy)
    

if __name__ == '__main__':

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    n=int(input())
    a=[list(map(int, input().split())) for _ in range(n)]
    # for x in a:
    #     print(x)

    cnt=0
    sx=0
    sy=0
    ex=0
    ey=0
    min1=2147000000
    max1=0
    for i in range(n):
      for j in range(n):
          if a[i][j]>max1:
              max1 = a[i][j]
              ex=i
              ey=j
          if a[i][j]<min1:
              min1 = a[i][j]
              sx=i
              sy=j

    # print(sx,sy, ex,ey)
    DFS(sx,sy)
    print(cnt)

  
