import sys
import heapq
N = int(sys.stdin.readline().rstrip())
cards = []

for i in range(N):
    card = int(sys.stdin.readline().rstrip())
    heapq.heappush(cards, card)  # 힙 정렬을 위해서

count = 0
while cards:
    # 카드 길이가 1인 경우 종료
    if len(cards) == 1:
        break
    x = heapq.heappop(cards)  # 제일 작은값 pop
    y = heapq.heappop(cards)  # 제일 작은값 pop
    count += (x + y)
    heapq.heappush(cards, x + y)

print(count)

# 단순히 오름차순으로 정렬하여 순서대로 작은값 끼리 더하여 나아가려고 했지만 잘못된 그리디한 접근이였다.
# 두 개의 카드를 더했을 때, 이 값보다 작은 수의 카드가 존재할 수 있기 때문에 이것을 고려해야함.
# 따라서, 힙 정렬을 통해 문제를 풀 수 있었다.
