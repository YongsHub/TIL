def countMeasure(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count % 2 == 0:
        return True
    else:
        return False


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if countMeasure(i):
            answer += i
        else:
            answer -= i
    return answer
