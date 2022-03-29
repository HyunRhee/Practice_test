
sum = 0
def listProd(sum):
    a = [1,0,1]
    b = [1,1,2]
    for i in range(3):
        sum = a[i] * b[i] + sum
    return sum
print("값은 : {} ".format(listProd(sum)))

#아무리 고민해봐도 listProd(a,b)로 리턴하는 방법이 떠오르지 않아서 함수안에 a,b가 아닌 sum을 넣었습니다.