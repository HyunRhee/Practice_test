import sys

Filename = input("파일명을 입력하세요")

try:
    myFile = open(Filename, "r")
    count = 1
    for i in range(3):
        line = myFile.readline()
        print("{}:".format(count) + line, end="")
        count = count + 1
    myFile.close()
except FileNotFoundError:
    print("파일이 없습니다")


