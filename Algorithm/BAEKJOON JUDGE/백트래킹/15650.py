import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * (N + 1)
arr = [0] * (N + 1)
result = []


def permutation(k):
    if k == M:  # M과 같으면 종료
        res = arr[:M]
        res.sort()
        if res not in result:
            result.append(res)
        return None

    for i in range(1, N + 1):
        if visited[i] is False:  # 방문 안한 숫자라면
            visited[i] = True
            arr[k] = i
            permutation(k + 1)
            visited[i] = False


permutation(0)
for row in result:
    print(*row)
