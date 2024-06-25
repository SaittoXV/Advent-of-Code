import re

with open("Day 3\inputTest.txt") as f:
    fileInput = f.read()

totalValue = 0

fileInput = fileInput.replace("."," ")
fileInput = re.sub("[*#+$/=&!@%^()-]","-",fileInput) 
# [0-9]|[*#+$/=&!@%^()-]

for countList, value in enumerate(fileInput.split("\n")):
    print(value + " -> " +  str(countList))
    fullNumber = ""
    for countString, number in enumerate(value):
        if number.isdigit():
            fullNumber = fullNumber + number
            if fileInput.split("\n")[countList][countString] == " " or value[countString+1] == " ":
                print("Yes the neighbor is empty")