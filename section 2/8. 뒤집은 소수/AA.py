import sys
# sys.stdin = open('in1.txt', 'rt')

cnt = int(input())
num = list(map(int, input().split()))
# cnt = 10
# print(cnt, num)

def reverse(x):
  tmp = list(str(x))
  tmp.reverse()
  tmp = int(''.join(tmp))
  return tmp

def isPrime(x):
  if x == 1: 
    return False

  for j in range(2, x//2+1):
    if x%j == 0:
      return False
  return True


for i in range(cnt):
  result = reverse(num[i])
  # print(result, isPrime(result))
  if(isPrime(result)):
    print(result, end=' ')


