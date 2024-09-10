n, m = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, input())))


def dfs(x, y):
  if 0>x or x>=n or y<0 or y>=m:
    return False
    
  if graph[x][y] == 1:
    return False
  else:
    graph[x][y] = 1
    dfs(x - 1, y) # 상 방향으로 이동
    dfs(x + 1, y) # 하 방향으로 이동
    dfs(x, y - 1) # 좌 방향으로 이동
    dfs(x, y + 1) # 우 방향으로 이동
    return True


result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)