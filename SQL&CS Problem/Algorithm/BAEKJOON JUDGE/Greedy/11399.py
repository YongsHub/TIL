import sys
N = int(sys.stdin.readline().rstrip())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

answer = 0
current = 0
for value in times:
    current += value
    answer += current

print(answer)
