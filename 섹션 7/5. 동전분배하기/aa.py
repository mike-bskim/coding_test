import sys
# sys.stdin=open('in1.txt', 'rt')
# input=sys.stdin.readline

def DFS(L):
    global min1

    # if max(money)> total/2: # 한개의 숫자가 다른 숫자보다 월등히 크면 로직오류 발생.
    #     return

    if L == n:
        dif = max(money) - min(money)
        if (dif) < min1:
            tmp = set(money)
            if len(tmp) == 3:
                min1 = dif
                # print(money, min1)

    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]
            


if __name__ == '__main__':
    n = int(input())
    coin=list()
    money=[0]*3
    min1=2147000000
    x=list()
    for _ in range(n):
        coin.append(int(input()))

    total=sum(coin)
    # print(n, coin, total)
    DFS(0)
    print(min1)
