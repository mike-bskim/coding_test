import sys
# sys.stdin=open('in3.txt', 'rt')
# input=sys.stdin.readline


def DFS(L, sum):
    global min1

    if sum > c or L>min1:
        return
    if sum == c:
        if L < min1:
            min1=L
            # print(min1)
            # sys.exit(0)
            # return

    else:
        for i in range(n):
            DFS(L+1, sum+a[i])


if __name__ == '__main__':
    # n = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    c = int(input())
    # print('input: ', n, a, c)

    min1=2147000000
    DFS(0,0)
    print(min1)

