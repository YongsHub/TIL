# 배열을 90도 회전하는 구현을 기억하자!
def rotateArray(key):
    n = len(key)  # 행 길이
    m = len(key[0])  # 열 길이
    newArray = [[0] * n for _ in range(m)]  # 새로운 배열

    for i in range(n):
        for j in range(m):
            newArray[j][n - i - 1] = key[i][j]
    return newArray


def check(lock):
    length = len(lock) // 3

    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]  # 자물쇠 크기를 3배로 키운다.

    # 커진 자물쇠의 정 가운데에 원래 값 배정
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for _ in range(4):
        key = rotateArray(key)  # 90도 회전
        # 배열의 끝까지만 확인하면 되니까 * 2배를 한 것.
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock):
                    return True

                # 키와 자물쇠가 일치하지 않다면
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
