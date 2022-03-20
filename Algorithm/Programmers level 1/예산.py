def solution(d, budget):
    answer = 0
    count = 0
    d.sort()  # 부서별 신청 금액 오름차순으로 정렬

    for i in d:
        answer += i
        count += 1
        if answer > budget:
            answer -= i
            count -= 1
            return count

    return count
