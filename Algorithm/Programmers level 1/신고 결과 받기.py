def solution(id_list, report, k):
    answer = []
    reports = dict()
    stop_users = dict()

    for i in id_list:
        reports[i] = []
        stop_users[i] = 0

    for i in report:
        name_A, name_B = i.split(' ')
        if name_B not in reports[name_A]:
            reports[name_A].append(name_B)
            stop_users[name_B] += 1

    real_stop = [i for i in stop_users if stop_users[i] >= k]
    real_list = [i for i in list(reports.values())]

    for lst in real_list:
        count = 0
        for name in real_stop:
            if name in lst:
                count += 1
        answer.append(count)

    return answer
