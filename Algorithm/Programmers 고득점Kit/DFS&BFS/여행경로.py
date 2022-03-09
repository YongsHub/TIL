from collections import deque


def bfs(tickets):
    queue = deque([])  # 데큐 선언
    queue.append(('ICN', 'ICN'))
    answer = []

    while queue:
        visit, arrived = queue.popleft()  # 큐에 들어있는 도시 pop
        temp = []
        if len(tickets) == 0:
            answer.append(arrived)
            return answer

        for start, arrive in tickets:
            if arrived == start:  # 도착한 공항 목록이 같을 때
                temp.append((start, arrive))

        if len(temp) == 0 and len(tickets) > 0:
            answer.pop()
            for start, arrive in tickets:  # 티켓의 목적지가 출발지가 되는 경우가 존재하지 않을 때
                if visit == start:
                    temp.append((start, arrive))
            tickets.append([visit, arrived])

        temp.sort(key=lambda x: x[1])  # 경우가 여러 개인 경우 알파벳으로 정렬
        info = temp[0]
        answer.append(info[0])
        queue.append((info[0], info[1]))
        tickets.remove([info[0], info[1]])


def solution(tickets):
    answer = bfs(tickets)
    return answer
