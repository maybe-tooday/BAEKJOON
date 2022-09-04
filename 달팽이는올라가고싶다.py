from sys import stdin
import math

A, B, V = map(int,stdin.readline().rstrip().split())

N = math.ceil((V - A)/(A - B) + 1)

print(N)