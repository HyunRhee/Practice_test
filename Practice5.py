n = float(input("Enter temperature: " ))
t = input("Convert to (F)ahrenheit or (C)elsius?")

if  t == "C":
    c = (5.0/9.0) * (n-32)
    print("{} F = {} C".format(n,c))

elif t == "F":
     f = (9.0/5.0) * (n) + 32
     print("{} C = {} F".format(n,f))