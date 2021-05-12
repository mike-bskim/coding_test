import sys
# sys.stdin = open('in4.txt', 'rt')

cnt = int(input())
math = list(map(int, input().split()))
avg = round(sum(math) / cnt)

new_val = float('inf')
new_idx = 0

for idx, val in enumerate(math):
  gap = abs(avg - val)
  new_gap = abs(avg - new_val)
  # print('>>>new_idx:{}, new_val:{}, idx:{}, val:{}, gap:{}, new_gap:{}'.format(new_idx, new_val, idx, val, gap , new_gap))
  if( gap < new_gap):
    new_val = val
    new_idx = idx
  elif(gap == new_gap):
    if val > new_val:
      new_val = val
      new_idx = idx

print(avg, new_idx+1)
