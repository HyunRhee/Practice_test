import math,random,sys

#1번

# a = int(input("자연수 a 를 입력하세요"))
# b = 0;
# sum = 0;
# for b in range(1,a+1,1):
#     sum = sum + b;
#
# print("1부터 자연수 {} 까지의 합은 : {}".format(a,sum))

#2번

# a = int(input("자연수 a까지의 짝수들의 합 :"))
# b = 0;
# sum = 0;
#
# for b in range(2,a+1,2):
#     sum = sum + b ;
# print("자연수 {}까지의 짝수의 합 :{}".format(a,sum))

#3번

# def fac():
#     a = 0
#     f = int(input("n!를 할까요? n을 입력하세요"))
#     result = 1
#     for a in range(1,f+1,1):
#         result = result * a
#     print("{}! : {}".format(f, result))
#
# fac()

#5번

# n = float(input("Enter temperature: " ))
# t = input("Convert to (F)ahrenheit or (C)elsius?")
#
# if  t == "C":
#     c = (5.0/9.0) * (n-32)
#     print("{} F = {} C".format(n,c))
#
# elif t == "F":
#      f = (9.0/5.0) * (n) + 32
#      print("{} C = {} F".format(n,f))

#6번

# r = float(input("반지름을 입력하세요"))
# S = 4.0 * (math.pi) * (math.pow(r,2))
# V = (4.0/3.0) * (math.pi) * (math.pow(r,3))
# print("반지름:{} 겉면적: {} 부피:{}".format(r,S,V))

#10번

# def listProd():
#     a = [1, 0, 1]
#     b = [1, 1, 2]
#
#     sum1 = a[0] * b[0]
#     sum2 = a[1] * b[1]
#     sum3 = a[2] * b[2]
#     return print(sum1+sum2+sum3)
# listProd()

#10번

# a = 0
# c = 1
# c1 = 0
# while a == 0:
#     n1 = random.randint(1, 9)
#     n2 = random.randint(1, 9)
#     answer = n1 * n2
#     youranswer = int(input("{} * {} 는 무엇입니까?".format(n1,n2) ))
#     if answer == youranswer:
#         print("정답입니다\n")
#         c1 = c1 + 1
#     else:
#         print("오답입니다\n")
#     t = input("계속하시겠습니까?\ny,n 로 입력하세요")
#     if t == "y":
#         a = 0
#         c = c+1
#     elif t == "n":
#         a = 1
#         p = float(c1/c) * 100
#         print("정답률은 {} 퍼센트입니다".format(p))

#11번

try:
    myFile = open("a.txt", "r")
except FileNotFoundError:
    print("파일이 없습니다")
myFile = open("a.txt", "r")

line = myFile.readline()
while line !="":
    print(line)
    line = myFile.readline()
myFile.close()




