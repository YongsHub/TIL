import sys
f = sys.stdin.readline
N, M = map(int, input().split())
balls = []
weights = list(map(int, f().split()))
for i in range(1, N + 1):
    balls.append((i, weights[i - 1]))

result = 0
for i in range(len(balls)):
    for j in range(i + 1, len(balls)):
        A = balls[i]
        B = balls[j]
        if A[1] != B[1]:
            result += 1

print(result)
