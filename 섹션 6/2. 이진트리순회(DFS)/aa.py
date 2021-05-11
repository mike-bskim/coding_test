import sys
# import heapq as hq
# sys.stdin = open('input.txt', 'rt')

# 전위순회 방식(print, DFS, DFS)
# 중위순회 방식(DFS, print, DFS)
# 후위순회 방식(DFS, DFS, print), 병합정렬인경우 
def DFS(x): 
  if x>7:
    return
  else:
    DFS(x*2)
    DFS(x*2+1)
    print(x, end=' ')


if __name__ == "__main__":
  # n = int(input())
  DFS(1)
# print(n)
# print(n%2)

