from collections import defaultdict


def timeTomin(str1):
    return int(str1.split(':')[0]) * 60 + int(str1.split(':')[1])


def minTotime(time):
    return "%02d:%02d" % (time//60, time % 60)


def shuttleTime(n, t, start="09:00"):
    shuttle = []
    shuttle.append(timeTomin(start))
    for i in range(n - 1):
        shuttle.append(shuttle[-1] + t)
    return shuttle


def solution(n, t, m, timetable):
    answer = ''
    RunningTime = defaultdict(list)
    crew = sorted([timeTomin(t) for t in timetable if t != "23:59"])  # 오름차순 정렬
    shuttle = shuttleTime(n, t)
    assign = defaultdict(list)
    # 1. crew원들 배정하기
    for crew_t in crew:
        for shuttle_t in shuttle:
            if len(assign[shuttle_t]) == m:
                continue
            else:
                if crew_t <= shuttle_t:
                    assign[shuttle_t].append(crew_t)
                    break
    # 2. crew 오름차순 정리 후 빈 list라면 shuttle 마지막 버스에 추가하고 return
    # or 마지막 셔틀 버스 운행 시간에 비어있다면
    if len(crew) == 0 or len(assign[shuttle[-1]]) == 0:
        return minTotime(shuttle[-1])

    # 마지막 셔틀 버스의 탑승 크루원 time - 1분
    lastShuttle_t = list(assign.values())[-1][-1] - 1

    if len(assign[shuttle[-1]]) < m:  # 마지막 셔틀 타임에 인원이 꽉 차있지 않다면
        return minTotime(shuttle[-1])

    return minTotime(lastShuttle_t)
