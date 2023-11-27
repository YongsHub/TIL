# 첫 번째로 공격받는 SCV 체력 9 잃음
# 두 번째 3
# 세 번째 1
import sys
from itertools import permutations
input = sys.stdin.readline
# 1 <= N <= 3
N = int(input().rstrip())
scv = list(map(int, input().split()))
cases = list(permutations([9, 3, 1]))
temp = [0] * 3
answer = int(10e9)

def dfs(cnt, a, b, c):
    global answer
    check = 0
    
    if a <= 0 and b <= 0 and c <= 0:
        return 
    else:
        for case in cases:
            if cnt + 1 < answer:
                answer = min(answer, dfs(cnt + 1, a - case[0], b - case[1], c - case[2]))
        return answer

for i in range(N):
    temp[i] = scv[i]
print(dfs(0, temp[0], temp[1], temp[2]))