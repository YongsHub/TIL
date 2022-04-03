from collections import defaultdict


def search(block, _type, idx, visited):
    row, col = idx
    #우, 하, 좌, 상
    dx = [0, 1, 0]
    dy = [1, 0, -1]
    tup = []
    tup.append((row, col))
    for i in range(3):  # 표기된 방향으로 2*2인지 확인하는 작업
        row = row + dy[i]
        col = col + dx[i]
        # 범위 벗어나는 경우
        if row < 0 or row >= len(block) or col < 0 or col >= len(block[row]):
            return visited, False
        if block[row][col] != _type:  # 타입 아닌 경우
            return visited, False
        else:
            tup.append((row, col))
    visited.extend(tup)  # 중복되지 않는 값 뒤에 추가
    return visited, True


def changeValue(block):  # X로 변경된 값 제외하고 추가
    newBlock = defaultdict(list)
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] != -1:
                newBlock[i].append(block[i][j])

    return newBlock


def solution(m, n, board):
    answer = 0
    block = defaultdict(list)
    board = reversed(board)
    board = [list(boards) for boards in board]

    for i in range(n):
        for j in range(m):
            block[i].append(board[j][i])

    while True:
        visited = []
        count = False
        # 전체 순회하면서 2*2가 지워지는지 확인
        for i in range(len(block)):
            for j in range(len(block[i])):
                visited, check = search(block, block[i][j], (i, j), visited)
                if check:
                    count = True
        if count == False or len(block) == 0:
            break
        else:
            answer += len(set(visited))
        for row, col in visited:
            block[row][col] = -1

        block = changeValue(block)
        print(block)
    return answer
