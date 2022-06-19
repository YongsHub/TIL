# 상, 하, 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []


def dfs(visited, grid, start, end, cnt):
    if start == len(grid) - 1 and end == len(grid[0]) - 1:
        answer.append(cnt)
        return False

    for i in range(4):
        nx = start + dx[i]
        ny = end + dy[i]

        # 방문한 노드거나 인덱스가 범위를 벗어난다면
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or visited[nx][ny]:
            continue
        else:
            visited[nx][ny] = True
            cnt += 1
            dfs(visited, grid, nx, ny, cnt)


def solution(grid, k):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    # 강은 방문으로 초기화
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                visited[i][j] = True

    visited[0][0] = True
    dfs(visited, grid, 0, 0, 0)
    return answer


answer = solution(["..FF", "###F", "###."], 3)
print(answer)
