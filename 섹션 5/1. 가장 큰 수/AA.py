import sys
# from collections import deque
# sys.stdin = open('in2.txt', 'rt')

# n = int(input())
a, n = (map(int, input().split()))
a = list(map(int, str(a)))

result = []

for i in range(len(a)):
  while result and n>0 and (result[-1]) < (a[i]):
    result.pop()
    n -= 1
  result.append(a[i])

if n!=0:
  result=result[:-n]
print(''.join(map(str, result)))



# sys.stdin = open('input.txt', 'rt')

# a, n = (map(int, input().split()))
# a = list(map(int, str(a)))
# print(n, a)

# result=[]

# for i in range(len(a)):
#   while result and n>0 and result[-1]<a[i]:
#     result.pop()
#     n -= 1
#   result.append(a[i])
#   print(result, n)

# if n!=0:
#   result=result[:-n]
# print(result) 

# for x in result:
#   print(x, end='')

# result = ''.join(map(str, result) )
# print()
# print(result)

