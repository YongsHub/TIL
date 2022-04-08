def timeToInt(start, end):  # HH:MM -> 몇분 차이인지 확인하기 위한 함수
    min1 = int(start[0:2]) * 60 + int(start[3:])
    min2 = int(end[0:2]) * 60 + int(end[3:])
    return min2 - min1


def makeToLong(notes, length):
    while True:
        notes = notes * 2
        if len(notes) > length:
            return notes


def makeSmall(note):
    dictionary = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for key in dictionary:
        note = note.replace(key, dictionary[key])  # replace는 존재하는 모든 것을 바꿔준다.
    return note


def solution(m, musicinfos):
    answer = []
    m = makeSmall(m)
    for musicinfo in musicinfos:
        start, end, title, notes = musicinfo.split(',')
        minutes = timeToInt(start, end)
        notes = makeSmall(notes)
        if len(notes) < minutes:
            notes = makeToLong(notes, minutes)
        notes = notes[0:minutes]  # 재생 시간 만큼 자른다.
        if m in notes:
            answer.append((minutes, title))
    if len(answer) == 0:
        return "(None)"

    answer.sort(key=lambda x: x[0], reverse=True)

    return answer[0][1]
