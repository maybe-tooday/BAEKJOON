from sys import stdin
A = []

for _ in range(9):

    Num = int(input())
    A.append(Num)
    if max(A) == Num:
        i = _ + 1

print(max(A) , i ,sep = '\n')
