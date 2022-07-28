x = int(input())
y = int(input())
#1 결과값 정의, xy동시판별 	시간68ms
# Quadrant = 0
# if x > 0 and y > 0 :
#     Quadrant = 1
# elif x < 0 and y > 0 :
#     Quadrant = 2
# elif x < 0 and y < 0 :
#     Quadrant = 3
# else :
#     Quadrant = 4
#
#print(Quadrant)

#2 바로 프린트, xy동시판별 	시간68ms

if x > 0 and y > 0 :
    print('1')
elif x < 0 and y > 0 :
    print('2')
elif x < 0 and y < 0 :
    print('3')
else :
    print('4')

# Quadrant = 0
# #3 안됬음.
# if x > 0 :
#     if y > 0 :
#         Quadran = 1
#     else : # y < 0
#         Quadran = 4
# else : # x < 0
#     if y > 0 :
#         Quadran = 2
#     else : # y < 0
#         Quadran = 3 