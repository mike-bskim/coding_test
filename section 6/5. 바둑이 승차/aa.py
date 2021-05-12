import sys
# sys.stdin=open("input.txt", "rt")


def DFS(v, sum, tsum):
    global result

    if sum + (total-tsum) < result:
        return

    if sum>l:
        return

    if v == n:
        if sum > result:
            result=sum

    else:
        DFS(v+1, sum+a[v], tsum+a[v])
        DFS(v+1, sum, tsum+a[v])

a = []
result=0

if __name__ == '__main__':
    l, n = map(int, input().split())
    for _ in range(n):
        a.append(int(input()))
    # print('input: ', l, n, a)
    total = sum(a)
    DFS(0,0,0)
    print(result)
