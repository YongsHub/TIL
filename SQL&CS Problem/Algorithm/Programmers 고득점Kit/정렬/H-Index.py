def solution(citations):
    citations.sort()
    for idx , citation in enumerate(citations):
        if citation >= len(citations) - idx : # h번 이상 인용된 논문이 h개 이상일 때
            return len(citations) - idx
    return 0