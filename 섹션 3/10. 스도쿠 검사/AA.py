import sys
# sys.stdin = open('in5.txt', 'rt')

# n = int(input())
a = [list(map(int, input().split())) for _ in range(9)]

# for b in a:
#   print(b)
#   print(sum(b))
result = True

for i in range(len(a)):
  result1 = [0]*10
  result2 = [0]*10
  for j in range(len(a)):
    result1[a[i][j]] = 1
    result2[a[j][i]] = 1

  if (sum(result1) != 9) or (sum(result2) != 9):
    # print('result1,2: ', i, sum(result1), sum(result2))
    result = False
    break
  else:
    for i in range(3):
      for j in range(3):
        result3 = [0]*10
        for k in range(i*3, i*3+3):
          for l in range(j*3, j*3+3):
            result3[a[k][l]] = 1
        
        if sum(result3) != 9:
          # print('result3: ', i, j, sum(result3))
          result = False
          break
      if result == False:
        break
    
if result==False:
  print('NO')
else:
  print('YES')


