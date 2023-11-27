import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# 내림차순 정렬
arr.sort(reverse=True)
start = 0
answer = 0
for i in range(M):
    if start >= K:
        answer += arr[1]
        start = 0
    else:
        answer += arr[0]
        start += 1
print(answer)

