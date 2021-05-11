import sys
# from collections import deque
sys.stdin = open('input.txt', 'rt')

# n = int(input())
a = input()
a = list(map(str, (a)))
# print(a)

tmp=[]
cnt = 0

# tmp.append(a[0])

for i in range(len(a)):
  # print(i, tmp, a[i])
  if(a[i]=='('):
    tmp.append(a[i])
  else:
    # print(a[i-1])
    if (a[i-1] =='('):
    # if (tmp[-1] =='('):
      tmp.pop()
      cnt += len(tmp)
    else:
      tmp.pop()
      cnt += 1
print(cnt)
  

# import sys
# sys.stdin=open("input.txt", "rt")

# s=input()
# cnt=0 #잘려진 총 조각 수
# box=0 #레이저를 맞게 되면 잘라지는 조각의 수

# for i in range(1, len(s)):
#     print(i, '>>', s[i])
#     if s[i-1]=='(' and s[i]==')':
#         cnt+=box
#     elif s[i-1]=='(' and s[i]=='(':
#         box+=1
#     elif s[i-1]==')' and s[i]==')':
#         box-=1
#         cnt+=1
        
# print(cnt)