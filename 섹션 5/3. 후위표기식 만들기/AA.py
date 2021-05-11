import sys
# from collections import deque
# sys.stdin = open('input.txt', 'rt')

# n = int(input())
a = input()
# print(a, 'aa')
result=[]
tmp = []

for x in a:
  if x.isdecimal():
    result.append(x)
    # print('decimal:', x)
  
  else:
    if x =='(':
      tmp.append(x)
    elif x == '*' or x == '/':
      while tmp and (tmp[-1]=='*' or tmp[-1]=='/'):
        result.append(tmp.pop())
      tmp.append(x)
    elif (x=='+' or x=='-'):
      while tmp and tmp[-1]!='(':
        # print('++--', x, tmp, tmp[-1])
        result.append(tmp.pop())
      tmp.append(x)
    elif x==')':
      # print(tmp)
      while tmp and tmp[-1] != '(':
        result.append(tmp.pop())
      tmp.pop()

while len(tmp) != 0:
  result.append(tmp.pop())
print(''.join(result))
# print(result)

# # print(tmp)
# op=[]

# for x in (result):
#   print('while', op)
#   if(x.isdecimal()):
#     op.append(x)
#     # print('idx:', idx)
#   else:
#     # print('idx:', idx)
#     c = x
#     b = int(op.pop())
#     a = int(op.pop())
#     if x == '*':
#       op.append(a*b)
#     elif x == '/':
#       op.append(a/b)
#     elif x == '+':
#       op.append(a+b)
#     elif x == '-':
#       op.append(a-b)
#     print(a,x,b)
#   print(op)






