import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
#도시 개수
N = int(input().rstrip())
#인접리스트
graph = [[] for _ in range(N + 1)]
#최소비용 초기화
dp = [INF for _ in range(N + 1)]
#버스 개수
M = int(input().rstrip())

#그래프 간선 정보
for _ in range(M):
    start, arrive, cost = map(int, input().split())
    graph[start].append((arrive, cost))


start, end = map(int, input().split())


def djikstra(start):
    dp[start] = 0
    priority = []
    #첫번째 start노드 방문처리
    for arrive, cost in graph[start]:
        if dp[arrive] > dp[start] + cost:
            dp[arrive] = dp[start] + cost
            heapq.heappush(priority, (dp[arrive], arrive)) # 비용, 도착노드

    while priority:
        current_cost, node = heapq.heappop(priority)
        if dp[node] < current_cost:
            continue
        for arrive, cost in graph[node]:
            if dp[arrive] > current_cost + cost:
                dp[arrive] = current_cost + cost
                heapq.heappush(priority, (dp[arrive], arrive))
    


djikstra(start)
print(dp[end])





