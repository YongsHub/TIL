# 최대 메모리 4MB : 에라토스테네스의 체로 해결하기에는 메모리 초과 문제가 발생한다.
import sys
input = sys.stdin.readline
n = int(input().rstrip())
def isPrime(a):
    if(a<2):
        return False
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return False
    return True

def dfs(num):
	# 목표 길이 도달 시 멈춤
    if len(str(num))==n:
        print(num)
    else:
        for i in range(10):
            temp=num*10+i
            if isPrime(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)
# length = int('1' + '0' * n)
# def is_prime(n):
#     if n <= 2:
#         if n == 2:
#             return True
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# for i in range(int('2' + '0' * (n - 1)), length):
#     start, end, isPrime = 0, n, True
#     num = str(i)
#     for j in range(n):
#         if not is_prime(int(num[start:end - j])):
#             isPrime = False
#             break
#     if isPrime:
#         print(i)
# 에라토스테네스의 체 메모리 초과
# prime = defaultdict(bool)
# prime[0], prime[1] = True, True
# for i in range(2, length):
#     if not prime[i]:
#         for j in range(i * 2, length, i):
#             prime[j] = True
