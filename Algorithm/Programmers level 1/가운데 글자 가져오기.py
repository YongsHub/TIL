def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        length = len(s) // 2
        answer += s[length - 1: length + 1]
    else:
        length = len(s) // 2
        answer += s[length]
    return answer
