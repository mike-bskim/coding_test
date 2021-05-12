import sys
sys.stdin = open('input.txt', 'rt')

n, cnt = list(map(int, input().split()))
a = [int(input()) for _ in range(n)]
# print(n, cnt, a)

s=0
e=max(a)
# print(e)

def count(size):
  cnt = 0
  for i in range(n):
    cnt += a[i]//size
  return cnt


while s<=e:
  mid = (s+e)//2
  # print(s, e, mid)
  if count(mid) >= cnt:
    # print('cnt: ', count(mid))
    res=mid
    s = mid + 1
  else:
    e = mid - 1

print(res)

