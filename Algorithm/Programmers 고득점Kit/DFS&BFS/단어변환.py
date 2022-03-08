from collections import deque


def bfs(begin, target, words, visited):
    queue = deque([])
    queue.append((begin, 0))
    length = len(begin) - 1

    while queue:
        value, depth = queue.popleft()
        if value == target:
            return depth
        for i in range(len(words)):
            count = 0
            if visited[i] == True:  # 방문한 단어라면 continue
                continue
            # queue에서 가져온 단어와 words에 있는 단어가 알파벳 비교
            for x, y in zip(words[i], value):
                if x == y:
                    count += 1
            if length == count:  # 하나의 알파벳 빼고 모두 같은 경우
                print(words[i])
                queue.append((words[i], depth + 1))
                visited[i] = True


def solution(begin, target, words):
    answer = 0
    if target not in words:  # target 단어가 words에 없다면
        return 0
    else:
        visited = [False] * len(words)
        answer = bfs(begin, target, words, visited)

    return answer
