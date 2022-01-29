n = int(input())

grades = []

for _ in range(n):
  name, grade = input().split()
  grades.append((name, int(grade)))

result = sorted(grades, key = lambda x: x[1])

for i in result:
  print(i[0], end=' ')
