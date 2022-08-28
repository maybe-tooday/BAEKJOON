from sys import stdin

T = int(input())

while T > 0:
    T -= 1
    A, B = map(int, stdin.readline().split())
    print(A+B)