from collections import deque
import sys
f = sys.stdin.readline
n, m, k, x = map(int, input().split())  # n은 도시 갯수, m 도로 갯수,최단 거리 k 출발 도시 번호 x

# 도시 갯수만큼 2차원배열의 행의 크기를 생성 n + 1인 이유는 -> 0번인덱스 고려x
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, f().split())  # 출발 도시와 도착 도시를 입력받음
    graph[start].append(end)

table = [-1] * (n + 1)  # 도시 개수 만큼 -1로 설정
table[x] = 0  # 출발지는 0으로 설정

q = deque([x])

while q:
    startCity = q.popleft()
    for i in graph[startCity]:
        if table[i] == -1:  # 처음 방문하는 도시라면
            table[i] = table[startCity] + 1
            # 최단 거리 갱신
            q.append(i)

check = False
for i in range(1, n + 1):
    if table[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
