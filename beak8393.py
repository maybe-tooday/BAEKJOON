# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

number = int(input())
sum = 0

for n in range(1,number+1):
    sum += n

print(sum)