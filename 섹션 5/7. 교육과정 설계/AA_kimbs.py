import sys
# from collections import deque
sys.stdin = open('input.txt', 'rt')

cc = input()
n = int(input())
# print(cc, n)


for i in range(n):
  idx=1
  plan=input()
  # print(plan)
  for x in plan:
    if x in cc[0:idx]:
      # print('x cc[0:idx], idx: ', x, cc[0:idx], idx)
      if x == cc[idx-1]:
        idx += 1
        if(idx >= len(cc)+1):
          print('#{} YES'.format(i+1))
          break
    else:
      if x in cc:
        # print('else>>', x, cc)
        print('#{} NO'.format(i+1))
        break

  else:
    print('#{} NO'.format(i+1))





