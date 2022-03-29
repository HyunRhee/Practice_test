import math,random

a = 0
c = 1
c1 = 0
while a == 0:
    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    answer = n1 * n2
    youranswer = int(input("{} * {} 는 무엇입니까?".format(n1,n2) ))
    if answer == youranswer:
        print("정답입니다\n")
        c1 = c1 + 1
    else:
        print("오답입니다\n")
    t = input("계속하시겠습니까?\ny,n 로 입력하세요")
    if t == "y":
        a = 0
        c = c+1
    elif t == "n":
        a = 1
        p = float(c1/c) * 100
        print("정답률은 {} 퍼센트입니다".format(p))