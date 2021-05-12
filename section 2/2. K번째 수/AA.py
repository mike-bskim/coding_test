import sys
# sys.stdin = open('in1.txt', 'rt')

case_cnt = int(input())
# print('case_cnt:', case_cnt)

for i in range(case_cnt):
  n, s, e, k = map(int, input().split())
  # print(n, s, e, k)
  test_list = list(map(int, input().split()))
  # print(test_list)
  test_target = test_list[(s-1):e]
  # print(test_target)
  test_target.sort()
  print('#{} {}'.format(i+1, test_target[k-1]))
