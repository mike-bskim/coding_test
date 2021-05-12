import sys
# sys.stdin = open('in1.txt', 'rt')

cnt = int(input())
num_list = list(map(int, input().split()))

def digit_sum(x):

  max = 0
  tmp_idx = 0

  for idx, val in enumerate(x):
    tmp_sum = 0
    tmp = str(val)
    for j in tmp:
      tmp_sum += int(j)

    if tmp_sum > max :
      max = tmp_sum
      tmp_idx = idx

  return max, tmp_idx, x[tmp_idx]

result_max, result_idx,  result= digit_sum(num_list)
# print(result, result_idx, result_max)
print(num_list[result_idx])
