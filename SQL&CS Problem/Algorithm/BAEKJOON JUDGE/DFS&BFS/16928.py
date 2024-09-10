import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# 사다리의 수, 뱀의 수
N, M = map(int, input().split())
visited = [0] * 101
for _ in range(N):
    x, y = map(int, input().split())
    visited[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    visited[x] = y

count = 10 ** 9


def dfs(start, cnt):
    notSnakeIdx = start
    global count

    if start >= 100:
        count = min(count, cnt)
        return

    for i in range(1, 7):
        start = start + 1
        if start >= 100:
            dfs(start, cnt + 1)
            return
        elif visited[start]:
            # 사다리인 경우
            if visited[start] > start:
                dfs(visited[start], cnt + 1)

            # 뱀을 타고가는데 주사위를 더 적게 돌린다.
        else:
            notSnakeIdx = start

    dfs(notSnakeIdx, cnt + 1)


dfs(1, 0)
print(count)
