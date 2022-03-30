def search(idx, board, _type, m, n):
    row, col = idx
    #우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    tup = []
    _board = []
    for i in range(4):  # 우, 하, 좌, 상 으로 탐색하면서 _type과 같은지 비교
        row = row + dx[i]
        col = col + dy[i]
        if row >= m or row < 0 or col >= n or col < 0:  # board 범위 벗어난다면
            return False
        if board[row][col] != _type:  # type과 같지 않다면
            return False
        else:
            tup.append((row, col))

    print('tup', tup)
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            if (i, j) in tup:
                continue
            row.append(board[i][j])
        _board.append(row)
    print('new board', _board)

    return True


def solution(m, n, board):
    answer = 0
    _type = ''
    for i in board:
        _type += i
    types = set(_type)  # 블록 종류
    board = [list(i) for i in board]  # board 요소 list로 변경
    print(board)
    count = 0
    for _type in types:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == _type:
                    if search((i, j), board, _type, m, n):
                        count += 1

    print(count)
    return answer
