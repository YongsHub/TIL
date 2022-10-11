import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
answer = 0
# for문 2번 돌리는 case
# for _ in range(N):
#     arr.append(list(map(int, input().split())))

# for i in range(N):
#     min_number = int(10e9)
#     for j in range(M):
#         min_number = min(min_number, arr[i][j])
#     answer = max(answer, min_number)
# print(answer)

for _ in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    answer = max(answer, min_value)
print(answer)