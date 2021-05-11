import sys
# sys.stdin = open('in0.txt', 'rt')

cnt = int(input())
num = []
score = []

for i in range(cnt):
  num.append(list(map(int, input().split())))

for i in range(cnt):
  num[i].sort()
  a,b,c = num[i]
  # print(a,b,c)

  if(a==b==c):
    score.append(10000 + a*1000)
  elif (a==b or b==c):
    score.append(1000 + b*100)
  elif (c==a):
    score.append(1000 + c*100)
  else:
    score.append(num[i][2]*100)

# print(num, score)
# print(type(score))
score.sort(reverse=True)
# print(max(score))
print(score[0])
