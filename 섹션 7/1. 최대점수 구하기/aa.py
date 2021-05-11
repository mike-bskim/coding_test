import sys
# sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline

def DFS(L, sum, tsum):
    global max1

    if tsum>m:
        return
    if L == n:
        if sum>max1:
            max1 = sum
        pass
    else:
        DFS(L+1, sum+p[L], tsum+t[L])
        DFS(L+1, sum, tsum)

if __name__ == '__main__':
    n, m = (map(int, input().split())) # 5 9
    # print('input: ', n, m)

    p=[]
    t=[]
    for _ in range(n):
        a,b = map(int, input().split())
        p.append(a)
        t.append(b)

    max1=0
    DFS(0,0,0)
    print(max1)
