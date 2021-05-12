import sys
# sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline


def DFS(L, s):
    global cnt
    if L == f:
        cnt+=1
        print(*res)

    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1)



if __name__ == '__main__':
    n, f = list(map(int, input().split())) # 4 2
    # print('input: ', n, f)

    res=[0]*f
    cnt=0
    DFS(0,1)
    print(cnt)