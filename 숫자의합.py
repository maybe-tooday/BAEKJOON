from sys import stdin
from collections import deque

N = int(stdin.readline())
word = deque()
word.extend(stdin.readline())
word_n = []
for n in range(N):
    word_n.append(int(word.popleft()))
print(sum(word_n))