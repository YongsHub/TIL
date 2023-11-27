def solution(n):
    answer = ["수"]
    for i in range(1, n):
        if answer[i - 1] == "수":
            answer.append("박")
        else:
            answer.append("수")
    return ''.join(answer)
