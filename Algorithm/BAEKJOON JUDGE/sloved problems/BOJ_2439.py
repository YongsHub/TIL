import sys
input = sys.stdin.readline
n = int(input().rstrip())
for i in range(n - 1, -1, -1):
    print((' ' * i) + '*' * (n - i))