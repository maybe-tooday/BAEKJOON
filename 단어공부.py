from sys import stdin

alp = [0]*26
word = stdin.readline().rstrip().upper()
for s in word:
    alp[ord(s)-65] += 1
max = 0
cnt = 0
whe = 0
for i in range(26):
    if max < alp[i]:
        max = alp[i]
        cnt = 1
        whe = i
    elif max == alp[i]:
        cnt += 1
#print(alp)
if cnt >= 2:
    print('?')
else:
    print(chr(whe+65))
