import sys
# sys.stdin = open('input.txt', 'rt')

n, cnt = list(map(int, input().split()))
a = [int(input()) for _ in range(n)]
a.sort()
# print(n, cnt, a)

s=1
e=a[-1]
res = 0
# print(s,e)

def check(dis):
  cnt = 1
  pos = a[0]
  for i in range(n):
    if (a[i]-pos)>= dis:
      cnt += 1
      pos = a[i]
    # print('cnt: {}, dis {}, i {} pos {}'.format(cnt, dis, i, pos))
  return cnt


while s<=e:
  mid = (s+e)//2
  # print('s {}, e {}, res {} mid {}'.format(s, e, res, mid))
  # print('mid {} check {}'.format(mid, check(mid)))
  if check(mid) >= cnt:
    res = mid
    s = mid + 1
  else:
    e = mid - 1
print(res)