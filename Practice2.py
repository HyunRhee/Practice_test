a = int(input("자연수 a까지의 짝수들의 합 :"))
b = 0;
sum = 0;

for b in range(2,a+1,2):
    sum = sum + b ;
print("자연수 {}까지의 짝수의 합 :{}".format(a,sum))