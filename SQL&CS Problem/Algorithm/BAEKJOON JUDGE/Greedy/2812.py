import sys
input = sys.stdin.readline


def solution(number, k):
    answer = ''
    index = 0

    while k != 0:
        if index == len(number)-1:
            number = number[:len(number)-1]
            index -= 1
            k -= 1
        elif int(number[index]) < int(number[index+1]):
            number = number[:index]+number[index+1:]
            if index != 0:
                index -= 1
            k -= 1
        else:
            index += 1

    answer = number

    return answer


N, K = map(int, input().split())
number = input().rstrip()
result = solution(number, K)
print(result)
