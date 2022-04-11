import sys
N, K = map(int, input().split())
values = []

for i in range(N):
    value = int(input())
    values.append(value)

values.sort(reverse=True)  # 내림차순 정렬

count = 0
for value in values:
    if K == 0:
        break

    count += (K // value)
    K = K % value
print(count)
