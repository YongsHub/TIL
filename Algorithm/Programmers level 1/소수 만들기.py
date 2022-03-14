from itertools import combinations


def isPrimeNumber(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    combies = list(combinations(nums, 3))
    combies = list(map(lambda x: x[0] + x[1] + x[2], combies))

    for summation in combies:
        if isPrimeNumber(summation):
            answer += 1

    return answer
