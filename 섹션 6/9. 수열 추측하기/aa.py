import sys
# sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline


def DFS(L, sum):

    if sum == f and L == n:
        print(*a)
        sys.exit(0)

    else:
        for i in range(n):
            if ch[i]==0:
                ch[i]=1
                a[L]=i+1
                DFS(L+1, sum+(a[L]*b[L]))
                ch[i]=0



if __name__ == '__main__':
    n, f = list(map(int, input().split())) # 3 2
    # print('input: ', n, f)

    a=[0]*n
    b=[1]*n
    ch=[0]*(n+1)
    for i in range(1,n):
        b[i]=b[i-1]*(n-i)//i
    # print(b)
    DFS(0,0)


    