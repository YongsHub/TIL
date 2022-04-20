from collections import deque
import sys

bottles = list(map(int, sys.stdin.readline().split()))
currents = [(0, 0), (1, 0), (2, bottles[-1])]
queue = deque([currents[-1]])

# while queue:
#     liter = queue.popleft()
print(queue)
