from collections import defaultdict


def findLong(dictionary, words):
    word = words[0]
    if len(words) == 1:
        return word
    for i in range(1, len(words)):  # 다음 문장 더해가면서 사전에 있는지 체크
        if word + words[i] in dictionary:
            word = word + words[i]
        else:
            break  # 없으면 무조건 멈춘다.

    return word


def solution(msg):
    answer = []
    dictionary = defaultdict(int)
    i = 1
    for alpha in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dictionary[alpha] = i
        i += 1

    words = list(msg)
    while True:
        if len(words) == 0:  # 남아있는 단어 없으면 종료
            break
        word = findLong(dictionary, words)  # 가장 긴 문자열 찾기
        if word in dictionary:
            for _ in range(len(word)):
                words.pop(0)  # 리스트로 만든 곳에서 삭제
            answer.append(dictionary[word])
            if len(words) > 0:  # 다음 글자가 남아있다면
                word = word + words[0]
                dictionary[word] = i  # w + c 해당 단어 사전에 등록
                i += 1
    return answer
