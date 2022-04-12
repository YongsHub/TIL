import sys
N = int(sys.stdin.readline().rstrip())
cards = []

for i in range(N):
    card = int(sys.stdin.readline().rstrip())
    cards.append(card)

count = 0
while cards:
    # 카드 길이가 1인 경우 종료
    if len(cards) == 1:
        break
    # 카드를 오름차순으로 정렬
    cards.sort()
    x = cards.pop(0)
    y = cards.pop(0)
    count += (x + y)
    cards.append(x + y)

print(count)
