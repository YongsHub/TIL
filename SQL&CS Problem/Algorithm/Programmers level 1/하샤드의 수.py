def solution(x):
    answer = True
    return answer if x % sum(map(int, str(x))) == 0 else False
