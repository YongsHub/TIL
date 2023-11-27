from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n): # 그래프 초기화
  graph[i] = list(map(int, input()))

# 상하좌우 움직이기 위한 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    for i in range(4): # 상하좌우 체크
      move_x = x + dx[i]
      move_y = y + dy[i]
      if move_x < 0 or move_x >= n or move_y < 0 or move_y >= m :
        continue
      if graph[move_x][move_y] == 0:
        continue
      if graph[move_x][move_y] == 1: # 첫 방문인 경우에만
        graph[move_x][move_y] = graph[x][y] + 1
        queue.append((move_x, move_y))

  return graph[n-1][m-1]

print(bfs(0, 0))