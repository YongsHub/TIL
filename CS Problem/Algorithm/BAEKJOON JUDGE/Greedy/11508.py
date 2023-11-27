N = int(input())
costs = []

for _ in range(N):
    costs.append(int(input()))

count = N // 3
count = count + (N % 3)

costs.sort(reverse=True)  # 내림차순으로 정렬
result = 0

for i in range(count):
    length = len(costs)
    if length > 0:
        Maxcost = costs.pop(0)
        length -= 1
        result += Maxcost

    cost2 = 0
    cost3 = 0
    if length > 0:
        cost2 = costs.pop(0)
        length -= 1
    if length > 0:
        costs.pop(0)

    result += cost2
print(result)
