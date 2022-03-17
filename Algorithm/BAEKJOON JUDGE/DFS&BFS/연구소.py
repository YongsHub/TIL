import sys
from itertools import combinations
from collections import deque
f = sys.stdin.readline


def BFS(laboratory, virus, N, M):
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]
    queue = deque([])

    for i in virus:
        queue.append(i)

    while queue:
        move_x, move_y = queue.popleft()

        for i in range(4):
            dx = move_x + x[i]
            dy = move_y + y[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= M:  # 범위 벗어난다면
                continue

            if laboratory[dx][dy] == 0:
                laboratory[dx][dy] = 2
                queue.append((dx, dy))

    count = 0
    for lst in laboratory:
        count += lst.count(0)
    return count


N, M = map(int, input().split())

laboratory = [list(map(int, f().split())) for _ in range(N)]
blanks = []
virus = []
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 0:  # 빈칸이라면
            blanks.append((i, j))

        if laboratory[i][j] == 2:  # virus라면
            virus.append((i, j))


walls = list(combinations(blanks, 3))  # 벽 3개를 세울 수 있는 경우의 수
count = []
for i in walls:
    # 벽을 세우는 과정
    laboratory[i[0][0]][i[0][1]] = 1
    laboratory[i[1][0]][i[1][1]] = 1
    laboratory[i[2][0]][i[2][1]] = 1

    count.append(BFS(laboratory, virus, N, M))

    laboratory[i[0][0]][i[0][1]] = 0
    laboratory[i[1][0]][i[1][1]] = 0
    laboratory[i[2][0]][i[2][1]] = 0

print(count)
print(max(count))
