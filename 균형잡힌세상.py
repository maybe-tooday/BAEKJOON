import sys
sys.stdin = open('균형잡힌세상.txt')

while True:
    word = input()
    if word == '.': #입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
        break
    stak = []
    print(word)
    # check_ = True
    for chr in word:
        if chr == '(' or  chr == '[':
            stak.append(chr)
        elif chr == ')' :
            if len(stak) != 0 and stak[-1] == '(':
                stak.pop()
            else:
                stak.append(')')
                break
        elif chr == ']':
            if len(stak) != 0 and stak[-1] == '[':
                stak.pop()
            else:
                stak.append(']')
                break
    if len(stak) == 0:
        print('yes')
    else:
        print('no')
