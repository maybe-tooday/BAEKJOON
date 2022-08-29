from sys import stdin

string = input()

alp = [-1]*26
for i in range(len(string)): #i:string인덱스, string[i] 인덱스값
    num_ = ord(string[i]) - 97
    if alp[num_] != -1:
        continue
    else:
        alp[num_] = i
print(*alp)