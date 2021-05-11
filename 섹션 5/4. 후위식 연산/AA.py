import sys
# from collections import deque
# sys.stdin = open('input.txt', 'rt')

# n = int(input())
aa = input()
# print(aa, 'aa')

# print(tmp)
op=[]

for x in aa:
  # print('while', op)
  if(x.isdecimal()):
    op.append(x)
    # print('idx:', idx)
  else:
    # print('idx:', idx)
    c = x
    b = int(op.pop())
    a = int(op.pop())
    if x == '*':
      op.append(a*b)
    elif x == '/':
      op.append(a/b)
    elif x == '+':
      op.append(a+b)
    elif x == '-':
      op.append(a-b)
    # print(a,x,b)
print(*op)






