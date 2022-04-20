import sys
from collections import deque


N, M = map(int, input().split())
deq = deque([i for i in range(1, N + 1)])
location = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(M):
    find = location[i]
    index = deq.index(find)
    if index <= (len(deq) // 2):
        answer += index
        deq.rotate(-index)
        deq.popleft()
    else:
        count = len(deq) - index
        answer += count
        deq.rotate(count)
        deq.popleft()

print(answer)
