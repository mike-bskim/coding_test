import sys
from collections import deque
sys.stdin=open("input.txt", "r")


# need=input()
# n=int(input())
# for i in range(n):
#     plan=input()
#     dq=deque(need)
#     for x in plan:
#         if x in dq:
#             if x!=dq.popleft():
#                 print("#%d NO" %(i+1))
#                 break
#     else:
#         if len(dq)==0:
#             print("#%d YES" %(i+1))
#         else:
#             print("#%d NO" %(i+1))







req=input()
n=int(input())
for num in range(n):
    timetable=input()
    s=0
    for i in timetable:
        if i in req:
            s+=1
            if i!=req[s-1]:
                print("#%d NO" %(num+1))
                break
    else:
        if s == len(req):
            print("#%d YES" %(num+1))
        else:
            print("#%d NO" %(num+1))



