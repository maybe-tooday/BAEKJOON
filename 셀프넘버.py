#생성자와 1~1만숫자

# 생성자가 없는 숫자를 셀프 넘버라고 한다. 
# 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
# 100이상의 셀프넘버를 해라.

def selfnumber(number):
    for _ in list(str(number)) :
        number += int(_)
    return number

selfnumset = set()

for i in range(10000):
    selfnumset.add(selfnumber(i))

for j in range(10000):
    if j in selfnumset:
        continue
    else:
        print(j)