from sys import stdin

N = int(stdin.readline())
A = []
A.extend(map(int,stdin.readline().split())) ##append, extend
max_A = max(A)
sum_A = sum(A)

print(sum_A / max_A * 100 / N)