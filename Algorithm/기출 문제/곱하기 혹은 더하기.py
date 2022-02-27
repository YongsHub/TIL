numbers = input()

current = int(numbers[0])
for number in numbers[1:]:
    if current == 0 or int(number) <= 1:  # number가 0이 올수도 있는 것을 고려하는 것을 잊지 말자.
        current = current + int(number)
    else:
        current = current * int(number)

    print(current)

print(current)
