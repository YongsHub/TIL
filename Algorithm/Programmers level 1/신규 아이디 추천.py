def solution(new_id):
    answer = ''
    id = list(new_id)

    big_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    check = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.']

    # 1단계
    for i in range(len(id)):
        if id[i] in big_alpha:
            id[i] = chr(ord(id[i]) + 32)
    # 2단계
    new_list = []
    for i in id:
        if i in check:
            new_list.append(i)
    # 3단계
    answer = ''.join(new_list)
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    answer = [i for i in answer]
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else ['.']
    if answer[-1] == '.':
        answer = answer[:-1]  # 원소가 하나일 때 answer[:-1]은 [] 반환
    # 5단계
    if len(answer) == 0:
        answer.append('a')

    # 6단계
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer.pop()

    # 7단계
    if len(answer) <= 2:
        while True:
            if len(answer) == 3:
                break
            answer += answer[-1]

    return ''.join(answer)
