import sys
# sys.stdin=open("input.txt", "rt")

def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if(ch[i] == 1):
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        # print(v, ch)
        DFS(v+1)
        ch[v]=0
        # print(v, ch)
        DFS(v+1)


if __name__ == '__main__':
    n = int(input())
    # a = list(map(int, input().split()))
    # print('input: ', n, a)
    ch=[0]*(n+1)
    DFS(1)