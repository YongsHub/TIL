from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline


def minValue(counts):  # 최소 count를 가지고 있는 key값 return
    minKey = 0
    minValue = 10 ** 9
    for count in counts:
        if counts[count] < minValue:
            minValue = counts[count]
            minKey = count
    return minKey


N, K = map(int, input().split())
names = deque(list(map(int, input().split())))
counts = defaultdict(int)
visited = [False] * (101)  # 전기용품이 K이하의 자연수로 사용 순서대로 주어짐.
num = 0

for name in names:  # 개수 count
    counts[name] += 1

for i in range(N):  # N만큼 일단 순서대로 콘서트에 꽂기
    name = names.popleft()
    counts[name] -= 1
    visited[name] = True


while names:  # 남은 전기용품 처리
    name = names.popleft()
    if visited[name]:
        counts[name] -= 1
    else:
        minKey = minValue(counts)
        visited[minKey] = False
        visited[name] = True
        num += 1
        counts[name] -= 1
print(num)
