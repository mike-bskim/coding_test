import sys
sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline

def DFS(x,y):
    global cnt

    if x==(n-1) and y==(n-1):
        cnt+=1
    
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n:

                if a[xx][yy]==0:
                    print(x,y, '>>> go >>>', xx,yy)
                    if xx==6 and yy==6: print('cnt:', cnt)
                    a[xx][yy]=1
                    DFS(xx,yy)
                    print(x,y, '<<<back<<<', xx,yy)
                    a[xx][yy]=0

if __name__ == '__main__':

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    # n=int(input())
    n=7
    a=[list(map(int, input().split())) for _ in range(n)]
    # for x in a:
    #     print(x)
    cnt = 0
    a[0][0]=1
    DFS(0,0)
    print(cnt)


