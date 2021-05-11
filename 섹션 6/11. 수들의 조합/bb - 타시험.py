import sys
sys.stdin=open('input1.txt', 'rt')
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
    n=900
    f=5
    a = [i for i in range(n)]
    t = n
    print('input: ', n, f, a, t)

    cnt=0
    DFS(0,0, 0)
    print(cnt)