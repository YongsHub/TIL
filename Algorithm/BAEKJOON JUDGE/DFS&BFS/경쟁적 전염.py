import sys
from collections import defaultdict
f = sys.stdin.readline


def BFS(examiner, virus, k):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    length = len(examiner)
    growth = defaultdict(list)

    for i in k:
        for x, y in virus[i]:
            for j in range(4):
                move_x = x + dx[j]
                move_y = y + dy[j]
                if move_x < 0 or move_x >= length or move_y < 0 or move_y >= length:  # 인덱스 벗어나면 continue
                    continue

                if examiner[move_x][move_y] == 0:  # 움직인 곳이 존재하는 바이러스가 아니라면
                    examiner[move_x][move_y] = i
                    growth[i].append((move_x, move_y))  # 증식된 위치 저장

    virus = growth
    return virus


n, k = map(int, input().split())
virus = defaultdict(list)


examiner = [list(map(int, f().split())) for _ in range(n)]
k = []
for i in range(n):
    for j in range(n):
        if examiner[i][j] != 0:
            virus[examiner[i][j]].append((i, j))
            if examiner[i][j] not in k:
                k.append(examiner[i][j])

k.sort()
s, x, y = map(int, f().split())

for i in range(s):
    virus = BFS(examiner, virus, k)

print(examiner[x - 1][y - 1])
