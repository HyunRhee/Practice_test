import math

r = float(input("반지름을 입력하세요"))
S = 4.0 * (math.pi) * (math.pow(r,2))
V = (4.0/3.0) * (math.pi) * (math.pow(r,3))
print("반지름:{} 겉면적: {} 부피:{}".format(r,S,V))