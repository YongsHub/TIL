import sys
f = sys.stdin.readline

n, m = map(int, input().split())
balls = list(map(int, f().split()))

array = [0] * 11


for i in balls:
    array[i] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)
