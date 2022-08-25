import sys
input = sys.stdin.readline
numbers = list(map(int, input().split()))
print(sum(list(map(lambda x: x ** 2, numbers))) % 10)