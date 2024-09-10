import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    R, S = input().split()
    result = list(map(lambda x: x * int(R), S))
    print(''.join(result))

