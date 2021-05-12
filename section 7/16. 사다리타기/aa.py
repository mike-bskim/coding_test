import sys
# sys.stdin=open('input.txt', 'rt')

def DFS(x,y):
  board[x][y]=2
  # print('>>>', x, y)

  if x==0:
    print(y)

  else:
    if 0<=(y-1)<10 and board[x][y-1]==1:
      DFS(x,y-1)
    elif 0<=(y+1)<10 and board[x][y+1]==1:
      DFS(x,y+1)
    else:
      DFS(x-1,y)

if __name__ == '__main__':
  board=[list(map(int, input().split())) for _ in range(10)]

  # for x in board:
  #   print(x)

  for y in range(10):
    if board[9][y] == 2:
      # print(y)
      DFS(9, y)