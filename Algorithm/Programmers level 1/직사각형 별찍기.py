a, b = map(int, input().strip().split(' '))
square = [['*'] * a for _ in range(b)]
for sqr in square:
    print(''.join(sqr))
