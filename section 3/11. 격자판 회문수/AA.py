import sys
# sys.stdin = open('input.txt', 'rt')

# n = int(input())
a = [list(map(int, input().split())) for _ in range(7)]

# for b in a:
#   print(b)
cnt = 0
check = []

for i in range(3):
  for j in range(7):
    tmp = a[j][i:i+5]
    if tmp == tmp[::-1]:
      cnt += 1
      # print('aa', i, j)
      # print('tmp:' , tmp)
    if all(a[i+k][j] == a[i+4-k][j] for k in range(2)):
      # print('bb', i,j)
      cnt += 1
      # for x in range(5):
      #   check.append(a[i+x][j])
      # print(check)
      
print(cnt)