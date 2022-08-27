A, B = map(int,input().split())
C = int(input())

CH, CM = C//60, C%60
AA = A + CH
BB = B + CM
while BB > 59:
    BB -= 60
    AA += 1
while AA > 23:
    AA -= 24
print(AA, BB)