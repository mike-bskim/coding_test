import sys
sys.stdin = open('in1.txt', 'rt')

cnt, th = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
print(type(cnt), type(th))

tmp_list = set()

for a in range(0, cnt - 2):
  for b in range(a+1, cnt - 1):
    for c in range(b+1, cnt):
      tmp_list.add(num_list[a] + num_list[b] + num_list[c])
      if (num_list[a] + num_list[b] + num_list[c]) == 152:
        print(num_list[a], num_list[b], num_list[c])

tmp_list = list(tmp_list)
tmp_list.sort(reverse=True)
print(tmp_list[th-1])
