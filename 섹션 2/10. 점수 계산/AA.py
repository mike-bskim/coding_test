import sys
# sys.stdin = open('in0.txt', 'rt')

cnt = int(input())
num = list(map(int, input().split()))
combo = 0
score = 0

for val in num:
  if val == 1:
    combo += 1
    score += combo
    # print('combo:', combo)
  else:
    combo = 0
    # print('combo:', combo)

print(score)
