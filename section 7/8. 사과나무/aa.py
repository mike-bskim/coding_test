import sys
from collections import deque
# sys.stdin=open('in2.txt', 'rt')
# input=sys.stdin.readline

if __name__ == '__main__':

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    n=int(input())
    a=list()
    for _ in range(n):
        a.append(list(map(int, input().split())))
    # print(n, a)
    # print(a[2][2])

    ch=[[0]* n for i in range(n)]
    ch[n//2][n//2]=1
    # print(ch)

    dQ=deque()
    dQ.append((n//2, n//2))
    sum=a[n//2][n//2]
    L=0

    while dQ:
        size=len(dQ)
        # print('while>>>', size, sum)
        if L == n//2:
            break
        for i in range(size):
            now=dQ.popleft()
            for j in range(4):
                x=now[0]+dx[j]
                y=now[1]+dy[j]
                # print(now, a[x][y])

                if ch[x][y] == 0:
                    ch[x][y]=1
                    sum+=a[x][y]
                    dQ.append((x, y))
        # for x in range(n):
        #     print(ch[x])
        # print('-------')
        L+=1
    print(sum)
    




