import sys

input = sys.stdin.readline


def find(p, v):
    if p[v] != v:
        p[v] = find(p, p[v])
    return p[v]


def union(p, x, y):
    a, b = find(p, x), find(p, y)
    p[b] = p[a]

        
edges = []
result = 0
cnt = 0
V, E = map(int, input().split())
p = [i for i in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# 가중치 오름차순으로 정렬
edges.sort(key=lambda x: x[2])

for edge in edges:
    #간선 개수가 V-1 : 즉 MST를 만족할 때, break
    if cnt == V - 1:
        break
    a, b, wt = edge

    #부모 노드가 서로 다르다면
    if find(p, a) != find(p, b):
        # union logic
        union(p, a, b)
        result += wt
        cnt += 1

print(result)