import sys
# sys.stdin=open("input.txt", "rt")
# input=sys.stdin.readline


def DFS(v):
    global cnt
    if v == n:
        cnt+=1
        for j in range(n):
            print(res[j], end=' ')
        print()
        # print(*res)
        return

    else:
        for i in range(L):
            res[v] = i+1
            DFS(v+1)


if __name__ == '__main__':
    L, n = map(int, input().split())
    # print('input: ', L, n)
    cnt=0
    res=[0]*n
    DFS(0)
    print(cnt)
