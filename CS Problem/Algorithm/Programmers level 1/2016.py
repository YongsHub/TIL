def solution(a, b):
    total = 0
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    order = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = a - 1
    day = b - 1

    total += sum(days[:month])
    total += day
    index = (total % 7)

    return order[index]
