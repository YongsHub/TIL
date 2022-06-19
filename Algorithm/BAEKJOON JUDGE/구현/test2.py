from collections import defaultdict


def splitData(datas):
    return datas.split(' ')[0], datas.split(' ')[1:]


def checkExtra(datas, client):  # 고객이 원하는 부가서비스가 요금제에 다 포함되어 있는지
    print(datas, client)
    for extra in client:
        if extra not in datas:
            return False
    return True


def check(datas, client):  # 최소의 요금제 찾기
    wantData = list(client.keys())
    for idx, data in enumerate(datas):
        if int(data) >= int(wantData[0]):
            result = checkExtra(datas[data], client[wantData[0]])
            print(result)
            if result:
                return idx + 1
    return 0


def solution(n, plans, clients):
    answer = []

    datas = defaultdict(list)
    prevKey = 0
    for plan in plans:
        data, services = splitData(plan)
        if prevKey != 0:
            datas[data] = datas[prevKey] + services
        else:
            datas[data] = services
        prevKey = data
    print(datas)
    for info in clients:
        data = info.split(' ')[0]  # clients의 원하는 요금제
        services = info.split(' ')[1:]  # 원하는 부가 서비스들
        client = defaultdict(list)
        client[data] = services
        number = check(datas, client)
        answer.append(number)
    return answer


solution(5, ["100 1 3", "500 4", "2000 5"], [
         "300 3 5", "1500 1", "100 1 3", "50 1"])
