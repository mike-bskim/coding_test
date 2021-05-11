import sys

sys.stdin = open("input.txt", "rt")

from collections import deque

answ = input()

n = int(input())

res = ""

for i in range(n) :

    tmp = list(map(str, input()))

    dq = deque(tmp)

    while dq :

        a = dq.popleft()

        if a in answ :

            res += a

    

    if res == answ :

        print("#%d YES" %(i+1))

    else :

        print("#%d NO" %(i+1))

    res = ""

    