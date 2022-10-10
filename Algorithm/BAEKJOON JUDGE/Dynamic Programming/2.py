import sys
input = sys.stdin.readline

S = input().rstrip()
C = list(map(int, input().split()))
N = int(input().rstrip())
start, end = 0, 0
answer = 0
while True:
    if start == N:
        break
    alpha = S[start]
    cost = [C[start]]
    for i in range(start + 1, N):
        if alpha == S[i]:
            cost.append(C[i])
            end = end + 1
        else:
            break
    if end - start > 0:
        if end - start == 1:
            answer += min(cost)
        else:
            cost.sort()
            answer += sum(cost[:end])
        start = end + 1
        end = start
    else:
        start += 1
        end += 1
print(answer)

        



