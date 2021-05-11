import sys
# sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline

def DFS(L, sum):
    global cnt
    if sum > t:
        return

    if L == k:
        if(sum == t):
            cnt+=1
            # print('>>>', x)

    else:
        for i in range(n[L]+1):
            x.append((p[L], i, 'limit:', n[L]))
            DFS(L+1, sum+(i*p[L]))
            x.pop()


if __name__ == '__main__':
    t = int(input())
    k = int(input())
    p=list()
    n=list()
    cnt=0
    x=list()
    for _ in range(k):
        a,b = map(int, input().split())
        p.append(a)
        n.append(b)

    # print(t, k, p, n)
    DFS(0,0)
    print(cnt)


# t=int(input())
# n=int(input())
# dy=[0]*(t+1)
# dy[0]=1
# for i in range(n):
#     a, b=map(int, input().split())
#     for j in range(t, 0, -1):
#         for k in range(1, b+1):
#             if(j-a*k<0): break
#             dy[j]+=dy[j-a*k]
# print(dy[t])