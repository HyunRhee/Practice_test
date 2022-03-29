
a = int(input("자연수 a 를 입력하세요"))
b = 0;
sum = 0;
for b in range(1,a+1,1):
    sum = sum + b;

print("1부터 자연수 {} 까지의 합은 : {}".format(a,sum))