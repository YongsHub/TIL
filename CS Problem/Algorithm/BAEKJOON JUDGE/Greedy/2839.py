import sys
N = int(sys.stdin.readline().rstrip())

count = 0
if N % 5 == 0:  # 입력된 N이 5로 나누어 떨어지는 경우는 바로 출력
    print(N // 5)
else:
    for _ in range(5000):
        if N < 3:
            break
        # N을 무조건 3으로 빼본다.
        N -= 3
        count += 1
        # 3을 빼본후, 5로 나누어지는지 체크
        if N % 5 == 0:
            count += (N // 5)
            N = N % 5
            break
    if N == 0:
        print(count)
    else:
        print(-1)
