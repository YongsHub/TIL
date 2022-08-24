import sys
input = sys.stdin.readline
words = list(map(lambda x: x.lower(), input().rstrip()))
sets = set(words)
maxValue = (0, 0)
count = 1
for alphabet in sets:
    cnt = 0
    for alpha in words:
        if alphabet == alpha:
            cnt += 1
    if cnt > maxValue[0]:
        maxValue = (cnt, alphabet)
        count = 1
    elif cnt == maxValue[0]:
        count += 1
if count > 1:
    print('?')
else: print(maxValue[1].upper())
