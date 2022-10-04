# 최대 메모리 4MB : 에라토스테네스의 체로 해결하기에는 메모리 초과 문제가 발생한다.
import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input().rstrip())
length = int('1' + '0' * n)
prime = defaultdict(bool)
prime[0], prime[1] = True, True
for i in range(2, length):
    if not prime[i]:
        for j in range(i * 2, length, i):
            prime[j] = True

for i in range(int('2' + '0' * (n - 1)), length):
    start, end, isPrime = 0, n, True
    num = str(i)
    for j in range(n):
        if prime[int(num[start:end - j])]:
            isPrime = False
            break
    if isPrime:
        print(i)
