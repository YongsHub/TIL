def solution(lines):
    start_time = []
    end_time = []
    answer = 0

    if len(lines) == 1:  # 로그 문자열이 1개밖에 없는 경우는 1개만 존재한다.
        return 1
    for i in lines:
        time = i.split(" ")
        end_time.append(get_end_time(time[1]))
        start_time.append(get_start_time(time[1], time[2]))

    for i in range(len(lines)):
        end = end_time[i]
        cnt = 0
        for j in start_time:
            if end > j - 1000:
                cnt += 1
        answer = max(cnt, answer)
    return answer


def get_end_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    sec = int(time[6:8])
    milliseconds = int(time[9:])

    return (hour + minute + sec) * 1000 + milliseconds


def get_start_time(time, during_time):
    time = get_end_time(time)
    during_time = int(float(during_time[:-1]) * 1000)
    return time - during_time + 1
