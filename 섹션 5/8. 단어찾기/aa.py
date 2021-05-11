import sys
# from collections import deque
# sys.stdin = open('input.txt', 'rt')

n = int(input())
word = []
poem = []
# print(n)

for _ in range(n):
  word.append(input())
word.sort()
# print(word)

for _ in range(n-1):
  poem.append(input())
poem.sort()
# print(poem)


for i in range(n-1):
  if(word[i] != poem[i]) :
    print(word[i])
    break
else:
  print(word[-1])