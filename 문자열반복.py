from sys import stdin
from collections import deque

T = int(stdin.readline())

for _ in range(T):
    ans = []
    word = deque(stdin.readline().rstrip())
    num_A = int(word.popleft())
    word.popleft()

    for n in word:
        for i in range(num_A):
            ans.append(n)
    print(*ans, sep = '')