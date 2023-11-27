import sys
f = sys.stdin.readline

data = f().rstrip()

newData = []
result = 0
for i in data:
    if i.isalpha():
        newData.append(i)
    else:
        result += int(i)

newData.sort()

newData.append(str(result))

print(''.join(newData))
