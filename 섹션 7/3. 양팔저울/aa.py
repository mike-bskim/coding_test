import sys
# sys.stdin=open('in1.txt', 'rt')
# input=sys.stdin.readline

def DFS(L, sum):
    global res

    if L == n:
        if (0<sum<=total):
            res.add(sum)
            # print('sum >>>', sum, x)

    else:
        # print('sum >>>',sum)
        x.append(s[L])
        DFS(L+1, sum+s[L])
        x.pop()
        x.append(-s[L])
        DFS(L+1, sum-s[L])
        x.pop()
        DFS(L+1, sum)


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    # print('input: ', n, s)
    x=list()
    
    total = sum(s)
    res=set()
    DFS(0,0)
    print(total - len(res))


