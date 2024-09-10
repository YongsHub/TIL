import sys
input = sys.stdin.readline
from collections import deque
#상,하,좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def get_test(n):
  column, row, y, x = map(int, input().split()) # 가로, 세로, 현재위치
  graph = []
  orders = []
  for _ in range(row):
    graph.append(list(map(int, input().split())))
  result = graph[x][y]
  k = int(input().rstrip())
  rotations = list(map(int, input().split()))
  rotations = deque(rotations)
  l = int(input().rstrip())
  for _ in range(l):
    direction, rotate_dir, counts = input().split()
    direction, rotate_dir, counts = direction, int(rotate_dir), int(counts)
    if rotate_dir == 1:
      rotations.rotate(counts)
    elif rotate_dir == 2:
      rotations.rotate(-counts)
      
      
    if direction == 'N':
      for i in range(rotations[0]):
        nx = x + dx[0]
        ny = y + dy[0]
        if nx < 0 or nx >= row or ny < 0 or ny >= column:
          break
        else:
          x, y = nx, ny
          if graph[x][y] > 0:
            result += graph[x][y]
    elif direction == 'S':
      for i in range(rotations[0]):
        nx = x + dx[1]
        ny = y + dy[1]
        if nx < 0 or nx >= row or ny < 0 or ny >= column:
          break
        else:
          x, y = nx, ny
          if graph[x][y] > 0:
            result += graph[x][y]
    elif direction == 'W':
      for i in range(rotations[0]):
        nx = x + dx[2]
        ny = y + dy[2]
        if nx < 0 or nx >= row or ny < 0 or ny >= column:
          break
        else:
          x, y = nx, ny
          if graph[x][y] > 0:
            result += graph[x][y]
    else:
      for i in range(rotations[0]):
        nx = x + dx[3]
        ny = y + dy[3]
        if nx < 0 or nx >= row or ny < 0 or ny >= column:
          break
        else:
          x, y = nx, ny
          if graph[x][y] > 0:
            result += graph[x][y]
      
    
  print('#'+str(n + 1), result, x, y)

case = int(input().rstrip()) #케이스
for i in range(case):
  get_test(i)


