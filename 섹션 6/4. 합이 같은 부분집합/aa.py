import sys
# sys.stdin=open("input.txt", "rt")

# def DFS(v):
#     sum = 0
#     if v == n+1:
#         for i in range(1, n+1):
#             if(ch[i] == 1):
#                 # print(i, end=' ')
#                 sum += a[i-1]
#         # print('>>>', sum)
#         if(sum == total-sum):
#             print('YES')
#             sys.exit(0)
#     else:
#         ch[v]=1
#         # print(v, ch)
#         DFS(v+1)
#         ch[v]=0
#         # print(v, ch)
#         DFS(v+1)


# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int, input().split()))
#     # print('input: ', n, a)
#     ch=[0]*(n+1)
#     total = sum(a)
#     DFS(1)
#     print('NO')


# sys.stdin=open("input.txt", "rt")
def DFS(v, sum):

    if v == n:
        if sum == (total-sum):
            # print('>>>', v, sum , n)
            print('YES')
            sys.exit(0)

    else:
        DFS(v+1, sum+a[v])
        DFS(v+1, sum)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # print('input: ', n, a)
    total = sum(a)
    DFS(0,0)
    print('NO')    