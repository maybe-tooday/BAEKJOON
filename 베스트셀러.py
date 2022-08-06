import sys
sys.stdin = open("베스트셀러.txt")

T = int(input())
board = [input() for _ in range(T)]

dic_ = dict()
for _ in range(T):
    if board[_] in dic_:
        dic_[board[_]] += 1
    elif board[_] not in dic_:
        dic_[board[_]] = 1

maxnum = max(dic_.values())
maxlist = []
for key in dic_:
    if dic_[key] == maxnum :
        maxlist.append(key)

maxlist.sort()
print(maxlist[0])