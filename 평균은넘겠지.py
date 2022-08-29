from sys import stdin
from collections import deque


N = int(stdin.readline())
while N > 0:
    N -= 1
    A = deque()
    A.extend(list(map(int,stdin.readline().split())))
    num_ = A.popleft()
    avr_A = sum(A) / num_ #평균 구하기

    cnt = 0
    for n in A:
        if avr_A < n:
            cnt += 1
    print(f'{round(cnt / num_, 5):.3%}')