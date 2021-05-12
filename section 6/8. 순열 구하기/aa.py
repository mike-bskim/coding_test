import sys
# sys.stdin=open('in1.txt', 'rt')
# input=sys.stdin.readline


def DFS(L):
    global cnt

    if L == a:
        cnt+=1
        print(*res)
        # return

    else:
        for i in range(n):
            if ch[i]==0:
                ch[i]=1
                res[L]=i+1
                DFS(L+1)
                ch[i]=0



if __name__ == '__main__':
    n, a = list(map(int, input().split())) # 3 2
    ch=[0]*(n)
    res=[0]*a
    cnt=0
    # print('input: ', n, a, ch)
    DFS(0)
    print(cnt)

    