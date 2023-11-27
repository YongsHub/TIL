from collections import deque


def solution(cacheSize, cities):
    answer = 0
    queue = deque([])
    _cities = []

    for city in cities:
        name = ''
        for alpha in city:
            if alpha.isupper():
                name += alpha.lower()
            else:
                name += alpha
        _cities.append(name)

    if cacheSize == 0:
        return 5 * len(cities)

    for city in _cities:
        if city not in queue:
            if len(queue) == cacheSize:  # 캐시 가 꽉찼다면
                queue.popleft()  # 가장 오래된 것 삭제
                answer += 5
                queue.append(city)
            else:
                answer += 5
                queue.append(city)
        else:  # city가 존재한다면
            answer += 1  # 실행시간 1 추가
            queue.remove(city)
            queue.append(city)  # 새로 갱신
    return answer
