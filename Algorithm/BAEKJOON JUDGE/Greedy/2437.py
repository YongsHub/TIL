# import sys
# f = sys.stdin.readline

# n = int(input())  # n 입력 받기
# coins = list(map(int, f().split()))  # 동전 입력받기
# coins.sort(reverse=True)

# minInteger = 1
# while True:
#     if minInteger not in coins:  # 주어진 동전에 없다면
#         for i in range(2, n + 1):
#             minValue = minInteger
#             count = 0
#             check = False
#             # 가지고 있는 코인이 정수 최솟값 보다 크다면
#             for j in range(n):
#                 if coins[j] > minValue:
#                     continue
#                 minValue -= coins[j]  # 만들어야 하는 정수값에서 가지고 있는 동전 요소를 뺀다.
#                 count += 1

#             if count == i and minValue == 0:
#                 check = True
#                 break
#         if check == False:  # 최솟값을 만들 수 없다면
#             print(minInteger)
#             break

#     minInteger += 1  # 최소 정수값을 증가시킴.

# 위의 코드는 시간 초과로 인해 비효율적인 코드이다 -> Greedy 식으로 접근하는 방식을 많이 익히자!
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for i in data:
    if target < i:
        break
    target += i

print(target)
