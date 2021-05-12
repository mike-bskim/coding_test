import sys
sys.stdin = open('input.txt', 'rt')

n, cnt = list(map(int, input().split()))
a = list(map(int, input().split()))
# print(n, cnt, a)

s=1
e=sum(a)
res = 0
# print(s,e)

def check(size):
  cnt = 1
  tmp = 0
  for i in range(n):
    tmp += a[i]
    if tmp > size:
      tmp = a[i]
      cnt += 1
    # print('cnt: {}, size: {}, i {} tmp {}'.format(cnt, size, i, tmp))
  return cnt


while s<=e:
  mid = (s+e)//2
  # print('s {}, e {}, res {} mid {}'.format(s, e, res, mid))
  # print('mid {} check {}'.format(mid, check(mid)))
  if mid >= max(a) and check(mid) <= cnt:
    res = mid
    e = mid - 1
  else:
    s = mid + 1
print(res)