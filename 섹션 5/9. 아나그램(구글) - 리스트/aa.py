import sys
# from collections import deque
# sys.stdin = open('in5.txt', 'rt')

a=input()
b=input()
# print(len(a))
# print(len(b))

a_dict = [0]*52
b_dict = [0]*52

for x in a:
  if x.isupper():
    # print(ord(x)-65, x, ord(x))
    a_dict[ord(x)-65] += 1
  else:
    # print(ord(x)-71, x, ord(x), '>>>')
    a_dict[ord(x)-71] += 1

for x in b:
  if x.isupper():
    b_dict[ord(x)-65] += 1
  else:
    b_dict[ord(x)-71] += 1

# print(a_dict)
# print(b_dict)

for i in range(len(a_dict)):
  if a_dict[i] != b_dict[i]:
    print('NO')
    break
else:
  print('YES')
