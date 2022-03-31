from collections import defaultdict


def search(block, _type, idx, visited):
    row, col = idx
    #우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    tup = []
    for i in range(4):  # 표기된 방향으로 2*2인지 확인하는 작업
        row = row + dy[i]
        col = col + dx[i]
        if row not in block or col < 0 or col >= len(block[row]):  # 범위 벗어나는 경우
            return visited, False
        if block[row][col] != _type:  # 타입 아닌 경우
            return visited, False
        else:
            if (row, col) not in visited:  # 중복된 값이 존재하는지 체크
                tup.append((row, col))
    visited.extend(tup)  # 중복되지 않는 값 뒤에 추가
    return visited, True


def changeValue(block):  # X로 변경된 값 제외하고 추가
    newBlock = defaultdict(list)
    for i in block:
        for j in range(len(block[i])):
            if block[i][j] == -1:
                continue
            else:
                newBlock[i].append(block[i][j])
    return newBlock


def solution(m, n, board):
    answer = 0
    block = defaultdict(list)
    board = reversed(board)
    board = [list(boards) for boards in board]
    types = []

    for i in range(n):
        for j in range(m):
            block[i].append(board[j][i])
            if 'A' <= board[j][i] <= 'Z':
                types.append(board[j][i])
    types = set(types)

    while True:
        visited = []
        count = 0
        for _type in types:
            for i in range(len(block)):
                for j in range(len(block[i])):
                    if _type == block[i][j]:  # 검색하려는 종류와 같다면
                        visited, check = search(block, _type, (i, j), visited)
                        if check:
                            count += 1
        if count == 0:
            return answer
        else:
            answer += len(visited)

        for row, col in visited:
            block[row][col] = -1

        block = changeValue(block)
    return answer
