with open("Day 1\input.txt") as f:
    fileInput = f.read()

numberDict = {'twone': '21', 'oneight': '18', 'nineight': '98', 'eightwo': '82', 'eighthree': '83', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
              'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

listText = fileInput.split("\n")
count = 0
for item in listText:
    for number in numberDict:
        if item.__contains__(number):
            listText[count] = listText[count].replace(
                number, numberDict[number])
    count += 1
totalSum = 0

for item in listText:
    wordNumber = ""
    for charItem in item:
        if charItem.isdigit():
            wordNumber = wordNumber + charItem
    print(wordNumber[0] + wordNumber[len(wordNumber)-1])
    totalSum = totalSum + int(wordNumber[0] + wordNumber[len(wordNumber)-1])
    print("Sum: " + str(totalSum))

print("THE TOTAL SUM IS " + str(totalSum))
