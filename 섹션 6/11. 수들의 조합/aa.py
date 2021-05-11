import sys
# sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline

def DFS(L, s, sum):
    global cnt

    if L == 0 and s > (n//2+1):
        return

    if L == f:
        # tmp = sum(res)
        # if tmp % t == 0:
        #     cnt+=1
        if (sum % t) == 0:
            cnt += 1

    else:
        for i in range(s, n):
            # res[L]=a[i]
            DFS(L+1, i+1, sum+a[i])



if __name__ == '__main__':
    n, f = (map(int, input().split())) # 5 3
    a = list(map(int, input().split())) # 2 4 5 8 12
    t = int(input()) # 6
    # print('input: ', n, f, a, t)

    cnt=0
    # res=[0]*f
    DFS(0,0, 0)
    print(cnt)