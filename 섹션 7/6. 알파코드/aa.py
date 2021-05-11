import sys
# sys.stdin=open('in2.txt', 'rt')
# input=sys.stdin.readline

def DFS(L, P):
    global cnt
    if L > n:
        return
    if L == n:
        for j in range(P):
            print(chr(res[j]+64), end='')
        cnt+=1
        print()

    else:
        for i in range(1,27):
            if a[L]==i:
                res[P]=i
                DFS(L+1, P+1)
            elif i>=10 and a[L]==i//10 and a[L+1]==i%10:
                res[P]=i
                DFS(L+2, P+1)


if __name__ == '__main__':
    a = list(map(int, input()))
    # print(a)

    cnt=0
    n=len(a)
    res=[0]*(n+3)
    a.append(-1)
    DFS(0,0)
    print(cnt)
