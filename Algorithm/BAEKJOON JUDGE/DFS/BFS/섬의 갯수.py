import sys

sys.setrecursionlimit(10 ** 6)


def dfs(graph, x, y):
    if x < 0 or x > (len(graph) - 1) or y < 0 or y > (len(graph[0]) - 1):
        return False
    if graph[x][y] == 1:
      # 상, 하, 좌, 우, 왼쪽위대각, 오른쪽위대각, 왼쪽 아래 대각, 오른쪽 아래 대각
        graph[x][y] = 0
        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x, y + 1)
        dfs(graph, x - 1, y - 1)
        dfs(graph, x - 1, y + 1)
        dfs(graph, x + 1, y - 1)
        dfs(graph, x + 1, y + 1)
        return True
    return False


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]  # 섬 갯수 바다 갯수

    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if dfs(graph, i, j):
                count += 1

    print(count)
