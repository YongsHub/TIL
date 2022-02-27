import sys
f = sys.stdin.readline

n = int(input())
data = list(map(int, f().split()))

count = 0  # 그룹 인원
result = 0  # 그룹 개수
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0


print(result)
