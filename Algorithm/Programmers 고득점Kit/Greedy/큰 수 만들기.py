def solution(number, k):
    answer = [] # 스택
    _k = k
    for num in number:
        while k > 0 and answer and answer[-1] < num: # k가 아직 0보다 크고, 스택이 비어있지 않고, 스택의 마지막이 num보다 작을 때
            answer.pop()
            k -= 1

        answer.append(num)


    return ''.join(answer[:len(number) - _k])