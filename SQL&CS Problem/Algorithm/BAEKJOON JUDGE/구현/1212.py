import sys
from collections import deque


N, M = map(int, input().split())
deq = deque([i for i in range(1, N + 1)])  # deq = deque([1~N])
location = list(map(int, sys.stdin.readline().split()))
print(deq, location)
answer = 0
locations = [1, 2, 3]
for i in range(M):
    find = location[i]  # M이 3이면, 3개를 뽑아야 한다.location[1] find = 2
    index = deq.index(find)  # deq.index(3) -> 0
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
