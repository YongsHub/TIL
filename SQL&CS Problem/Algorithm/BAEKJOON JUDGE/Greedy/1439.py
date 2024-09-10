data = input()

result = 0
count = 0
arrCount = []
for value in data:
    if value == '0':
        count = 0
    else:
        if count == 0:
            result += 1
        count += 1


arrCount.append(result)

result = 0
count = 0

for value in data:
    if value == '1':
        count = 0
    else:
        if count == 0:
            result += 1
        count += 1


arrCount.append(result)

print(min(arrCount))
