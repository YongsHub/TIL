def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def checkCorrect(p):
    check = [False for _ in range(len(p))]
    for i in range(len(p)):  # 균형잡힌 문자열이기 때문에 올바른 문자열인지 체크
        if p[i] == '(':
            check[i] = True
            if search(i, p, check) == False:
                break
    if False not in check:  # 올바른 문자열이라면 return
        return True
    else:
        return False


def search(start, p, check):
    for i in range(start + 1, len(p)):
        if p[i] == ')':
            if check[i] == True:  # 이미 True라면
                continue
            check[i] = True
            return True
    return False


def solution(p):
    answer = ''
    if p == '':  # 입력이 빈 문자열인 경우
        return ''

    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if checkCorrect(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += ''.join(u)

    return answer

# Solution 함수를 재귀로 돌리는 구현
# 균형잡힌 문자열에 대해 생각하는 솔루션
