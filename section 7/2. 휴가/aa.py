import sys
# sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline

def DFS(L, Psum):
    global max1

    if L>n+1:
        return
    if L == n+1:
        if Psum>max1:
            max1 = Psum
    else:
        if L <= n+1:
            DFS(L+t[L], Psum+p[L])
        DFS(L+1, Psum)

if __name__ == '__main__':
    n = int(input())
    # print('input: ', n)

    t=[]
    p=[]
    max1=0
    for _ in range(n):
        a,b = map(int, input().split())
        t.append(a)
        p.append(b)
    t.insert(0,0)
    p.insert(0,0)
    DFS(1,0)
    print(max1)

