import sys
input = sys.stdin.readline
N, M, L, K = map(int, input().split()) # 1 <= N, M <= 500,000, 1 <= K <= 100 N은 별똥별 떨어지는 구역의 가로길이, M은 세로, L은 트렘펄린 한 변의 길이 K는 별똥별 수
answer = K
coordinate = dict()
positions = []
for _ in range(K):
    x, y = map(int, input().split())
    positions.append((x, y))

for x, y in positions:
    for i in range(x - L, x + L + 1):
        if i < 0 or i + L > N or y + L > M:
            continue
        coordinate[(i, i + L, y, y + L)] = 0
    #제 2,4분면
    for i in range(x - L, x + L + 1):
        if i < 0 or i + L > N or y - L < 0:
            continue
        coordinate[(i, i + L, y - L, y)] = 0

for x, nx, y, ny in coordinate.keys():
    for dx, dy in positions:
        if x <= dx <= nx and y <= dy <= ny:
            coordinate[(x, nx, y, ny)] += 1
    answer = min(answer, K - coordinate[(x, nx, y, ny)])
print(answer)