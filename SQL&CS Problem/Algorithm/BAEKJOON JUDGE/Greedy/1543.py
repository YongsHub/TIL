import sys
input = sys.stdin.readline


def solution(words, find):
    tLength, fLength = len(words), len(find)
    count = 0
    visited = [0] * len(words)
    for i in range(tLength):
        if i + fLength > tLength:  # i + 찾는 단어의 길이가 전체 길이보다 크다면
            break
        if words[i] == finds[0] and not visited[i]:  # 주어진 문서의 단어가 finds 첫번째와 같다면
            check = True
            visited[i] += 1
            for j in range(1, fLength):
                if words[i + j] != find[j]:
                    check = False
                else:
                    visited[i + j] += 1
            if check:
                count += 1
                check = False
            else:
                visited[i: i + j + 1] = [0] * fLength
    return count


document = input().rstrip()

finds = input().rstrip()
result = solution(document, finds)
print(result)
