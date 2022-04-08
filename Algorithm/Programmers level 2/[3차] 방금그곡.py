def timeToInt(start, end):  # HH:MM -> 몇분 차이인지 확인하기 위한 함수
    min1 = int(start[0:2]) * 60 + int(start[3:])
    min2 = int(end[0:2]) * 60 + int(end[3:])
    return min2 - min1


def makeToLong(notes, length):
    types = ['A', 'C', 'D', 'F', 'G']
    lst = []
    for index, note in enumerate(notes):
        if note == '#':
            continue
        if note in types and index < len(notes) - 1 and notes[index + 1] == '#':
            lst.append(note + '#')
        else:
            lst.append(note)
    while True:
        lst = lst * 2
        if len(lst) > length:
            return lst


def makeList(m):
    types = ['A', 'C', 'D', 'F', 'G']
    lst = []
    for index, note in enumerate(m):
        if note == '#':
            continue
        if note in types and index < len(m) - 1 and m[index + 1] == '#':
            lst.append(note + '#')
        else:
            lst.append(note)
    return lst


def compare(m, notes):
    length = len(m)
    m = ''.join(m)
    total = len(notes)
    for index, note in enumerate(notes):
        if note == m[0] and index + length < total:
            arr = ''.join(notes[index:index + length])
            if arr == m:
                return True
    return False


def solution(m, musicinfos):
    answer = ''
    playingTime = 0
    startTime = 0
    m = makeList(m)
    for musicInfo in musicinfos:
        start, end, title, notes = musicInfo.split(',')
        minutes = timeToInt(start, end)
        if len(notes) < minutes:  # 악보 길이가 재생시간보다 짧다면
            notes = makeToLong(notes, minutes)
        else:
            notes = makeList(notes)[0:minutes]

        if compare(m, notes):
            if minutes > playingTime:
                answer = title
                playingTime = minutes
                startTime = int(start[0:2]) * 60 + int(start[3:])
            elif minutes == playingTime:
                continue
    if answer == '':
        answer = None

    return answer
