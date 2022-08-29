from sys import stdin

word = stdin.readline().strip()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for _ in croatia:
    word = word.replace(_,'0')

print(len(word))