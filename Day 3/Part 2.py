with open("Day 3\input.txt") as file:
    inputFileRow = file.readlines()

summationGearRatio = []

for indexRow, row in enumerate(inputFileRow):
    coordinateFirstChar = set()
    multiplyGearRatio = []
    for indexColumn, column in enumerate(row):
        if column.isdigit() or column != "*":
            continue
        for currentRow in [indexRow-1,indexRow,indexRow+1]:
            for currentColumn in [indexColumn-1,indexColumn,indexColumn+1]:
                if currentRow < 0 or currentRow >= len(inputFileRow) or currentColumn < 0 or currentColumn >= len(inputFileRow[currentRow]) or not inputFileRow[currentRow][currentColumn].isdigit():
                    continue
                while currentColumn > 0 and inputFileRow[currentRow][currentColumn-1].isdigit():
                    currentColumn -= 1
                coordinateFirstChar.add((currentRow,currentColumn))
        if len(coordinateFirstChar) < 2:
            coordinateFirstChar.clear()
        for row, column in coordinateFirstChar:
            fullString = ""
            while column < len(inputFileRow[row]) and inputFileRow[row][column].isdigit():
                fullString += inputFileRow[row][column]
                column +=1
            multiplyGearRatio.append(int(fullString))
        if len(multiplyGearRatio) != 0 and len(multiplyGearRatio)%2 ==0:
            productItem = 1
            for item in multiplyGearRatio:
                productItem = productItem * item
            summationGearRatio.append(productItem)
            multiplyGearRatio.clear()
            coordinateFirstChar.clear()
print(sum(summationGearRatio))