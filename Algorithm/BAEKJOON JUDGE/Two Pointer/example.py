import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = 0
cnt = 0
for i in range(N):
    summation = lst[i]
    end = i + 1
    while summation < M and end < N:
        summation += lst[end]  # start : end 까지의 합
        end += 1

    if summation == M:  # 합이 같다면
        cnt += 1  # 카운트 + 1
        summation = 0
print(cnt)

# 인덱스로 접근하려는 노력을 하자!
