import re

with open("Day 5\inputTest.txt") as file:
    fileInput = file.readlines()

seedList = []

seedLineItem = fileInput[0].split()

for item in seedLineItem:
    if item.isnumeric():
        seedList.append(item)

seedList.sort()
print(seedList)
