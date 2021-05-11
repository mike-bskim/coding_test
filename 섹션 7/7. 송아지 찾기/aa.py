import sys
from collections import deque
# sys.stdin=open('in2.txt', 'rt')
# input=sys.stdin.readline

if __name__ == '__main__':
    s, e = map(int, input().split())
    # print(s, e)

    MAX=10000
    ch=[0]*(MAX+1)
    dis=[0]*(MAX+1)
    ch[s]=1
    dis[s]=0
    dQ=deque()
    dQ.append(s)
    while dQ:
        now = dQ.popleft()
        if now==e:
            break
        for next in (now-1, now+1, now+5):
            if 0<next<=MAX:
              if ch[next]==0:
                    ch[next]=1
                    dQ.append(next)
                    dis[next]=dis[now]+1
    print(dis[now])
