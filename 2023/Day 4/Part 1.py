import re

with open("Day 4\input.txt") as file:
    inputFileRow = file.readlines()

listPoints = []

for row in inputFileRow:
    currentRow = re.sub("Card [0-9]+:","",row)
    cardOne = currentRow.split("|")[0].strip()
    cardTwo = currentRow.split("|")[1].strip()
    pointNumber = 0
    counter = 0
    for indexCardOne, itemCardOne in enumerate(cardOne.split()):
        for indexCardTwo, itemCardTwo in enumerate(cardTwo.split()):
            if itemCardOne.strip() == itemCardTwo.strip() and counter == 0:
                pointNumber +=1
                counter +=1
            elif itemCardOne.strip() == itemCardTwo.strip() and counter >0:
                pointNumber *=2
                counter +=1
    listPoints.append(pointNumber)
print(sum(listPoints))