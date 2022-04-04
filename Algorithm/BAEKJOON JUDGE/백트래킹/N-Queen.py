N = int(input())  # N 입력 받음


def makeVisited(chess, i, j, N):
    check = True
    for row in range(N):
        check = False
        for col in range(N):
            if row == i or col == j:  # 같은 행 또는 같은 열이라면
                check = True
                chess[row][col] = 1
                continue
            if row > i:
                checkRow = row - i
            else:
                checkRow = i - row

            if col > j:
                checkCol = col - j
            else:
                checkCol = j - col

            if checkRow == checkCol:
                check = True
                chess[row][col] = 1
    count = 0
    if check:  # True라면
        if i < N - 1:
            for col in range(len(chess[i + 1])):
                if chess[i + 1][col] == 0:
                    check = makeVisited(chess, i + 1, col, N)
                    if check:
                        count += 1
    return check, count


answer = 0
for i in range(N):
    chess = [[0] * N for _ in range(N)]  # 체스판 초기화
    chess[0][i] = 1  # 1로 초기화
    check, count = makeVisited(chess, 0, i, N)
    answer += count

print(answer)
