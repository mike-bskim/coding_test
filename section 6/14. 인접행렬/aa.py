import sys
sys.stdin=open('input.txt', 'rt')
# input=sys.stdin.readline

if __name__ == '__main__':
    n, f = (map(int, input().split())) # 6 9
    print('input: ', n, f)

    m = [[0]*(n+1) for _ in range(n+1)]
    # for x in m:
    #     print(x[1:])

    for _ in range(f):
        a,b,c = map(int, input().split())
        m[a][b] = c
    for i in range(1, n+1):
        print(*m[i][1:])
