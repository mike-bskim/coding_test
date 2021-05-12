import sys
# from collections import deque
# sys.stdin = open('input.txt', 'rt')

# a = list(map(str, input()))
# b = list(map(str, input()))
# a.sort()
# b.sort()
a=input()
b=input()
# print(a)
# print(b)

a_dict = {}
b_dict = {}

for x in a:
  a_dict[x] = a_dict.get(x, 0)+1
# print(a_dict)  

for x in b:
  b_dict[x] = b_dict.get(x, 0)+1
# print(b_dict)

for x, y in a_dict.items():
  if x in b_dict.keys():
    if y != b_dict[x]:
      print('NO')
      break
  else:
    print('NO')
else:
  print('YES')
