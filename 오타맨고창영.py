import sys
sys.stdin = open('오타맨고창영.txt','r')

T = int(input())

word = [list(input().split()) for _ in range(T)]
#print(word)

for i in range(T):
    num_ = int(word[i][0])
    str_ = word[i][1]
    string_ = str_[:num_-1] + str_[num_:]
    print(string_)