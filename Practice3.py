def fac():
    a = 0
    f = int(input("n!를 할까요? n을 입력하세요"))
    result = 1
    for a in range(1,f+1,1):
        result = result * a
    print("{}! : {}".format(f, result))

fac()