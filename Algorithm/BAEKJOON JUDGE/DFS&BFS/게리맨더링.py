import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
population = list(map(int, sys.stdin.readline().split()))
population.insert(0, 0)
graph = defaultdict(list)
for i in range(1, N + 1):
    lst = list(map(int, sys.stdin.readline().split()))
    graph[i] = lst[1:]

visited = [False] * (N + 1)
print(population)
print(graph)
