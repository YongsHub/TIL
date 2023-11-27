import sys
f = sys.stdin.readline

score = list(map(int, input()))

middleIndex = len(score) // 2

sum_1 = sum(score[0:middleIndex])
sum_2 = sum(score[middleIndex:])

if sum_1 == sum_2:
    print('LUCKY')
else:
    print('READY')
