def solution(str1, str2):
    str1 = list(map(lambda x: x.lower() if x.isupper() else x, str1))
    str2 = list(map(lambda x: x.lower() if x.isupper() else x, str2))
    setA = []
    setB = []
    andSet = []
    orSet = []

    # 두 글자씩 끊기
    length = len(str1) - 1
    for index, value in enumerate(str1):
        if index < length:
            if str1[index].isalpha() and str1[index + 1].isalpha() and str1[index + 1] != ' ':
                setA.append((str1[index], str1[index + 1]))

    length = len(str2) - 1
    for index, value in enumerate(str2):
        if index < length:
            if str2[index].isalpha() and str2[index + 1].isalpha() and str2[index + 1] != ' ':
                setB.append((str2[index], str2[index + 1]))

    if len(setA) == 0 and len(setB) == 0:  # 두 집합이 모두 공집합인 경우
        return 65536

    # 다중 집합의 교집합 구하기
    result = set(setA) & set(setB)
    for i in result:
        x = setA.count(i)
        y = setB.count(i)
        if x == 1 or y == 1:
            andSet.append(i)
        else:
            count = min(x, y)
            for _ in range(count):
                andSet.append(i)

    # 다중 집합의 합집합 구하기
    result = set(setA) | set(setB)
    for i in result:
        x = setA.count(i)
        y = setB.count(i)
        if x > 1 or y > 1:
            count = max(x, y)
            for _ in range(count):
                orSet.append(i)
        else:
            orSet.append(i)
    result = (len(andSet) / len(orSet)) * 65536
    return int(result)
