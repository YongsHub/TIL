def solution(board, moves):
    answer = 0
    dolls = [[] for _ in range(len(board) + 1)]

    for i in range(len(board)):
        for j in range(len(board) - 1, -1, -1):
            if board[j][i] == 0:
                continue
            dolls[i + 1].append(board[j][i])

    check = []
    for i in moves:
        if len(dolls[i]) > 0:
            check.append(dolls[i].pop())
            length = len(check)
            if length >= 2:
                if check[length - 1] == check[length - 2]:
                    check = check[0:length - 2]
                    answer += 2
    return answer
