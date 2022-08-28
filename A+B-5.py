from sys import stdin

A, B= 1, 1
while True:
    A, B = map(int,stdin.readline().split())
    if A == 0 and B == 0:
        break
    print(A + B)