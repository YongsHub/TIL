import sys
input = sys.stdin.readline
result = 1
for _ in range(3):
    result = result * int(input().rstrip())
result = str(result)
print(result.count('0'))
for i in range(1, 10):
    print(result.count(str(i)))