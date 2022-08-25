import sys
input = sys.stdin.readline
maxValue = (0, 0)
for i in range(1, 10):
    num = int(input().rstrip())
    if num > maxValue[0]:
        maxValue = (num, i)
print(maxValue[0])
print(maxValue[1])
