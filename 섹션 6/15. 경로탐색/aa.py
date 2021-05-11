import sys
sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline

def DFS(L):
    global cnt
    if L == n:
        cnt+=1
        print(*path)
    else:
        for i in range(1, n+1):
            if ch[i]==0 and m[L][i]==1:
                ch[i]=1
                path.append(i)
                DFS(i)
                ch[i]=0
                path.pop()
    

if __name__ == '__main__':
    n, f = (map(int, input().split())) # 5 9
    print('input: ', n, f)

    cnt=0
    path=[]
    path.append(1)
    m = [[0]*(n+1) for _ in range(n+1)]

    for _ in range(f):
        a,b = map(int, input().split())
        m[a][b] = 1
    ch=[0]*(n+1)
    ch[1]=1
    DFS(1)
    print(cnt)
