import re
with open("Day 4\inputTest.txt") as file:
    inputFile = file.readlines()

instancesCardsNumber = {}

def main():
    for indexRow, row in enumerate(inputFile):
        matchCase = []
        cardNumber = re.findall("Card [0-9]+",row)
        cardNumber = str(cardNumber[0])
        cardNumber = cardNumber.replace("Card","").strip()
        currentRow = re.sub("Card [0-9]+:","",row).strip()
        partOne = currentRow.split("|")[0]
        partOne = partOne.strip().split()
        partTwo = currentRow.split("|")[1]
        partTwo = partTwo.strip().split()
        for indexColumn, column in enumerate(partOne):
            for columnPartTwo in partTwo:
                if str(partOne[indexColumn]).strip() == str(columnPartTwo).strip():
                    matchCase.append(columnPartTwo)
        for length in range(int(cardNumber) + 1,len(matchCase) + int(cardNumber) + 1):
            print(str(cardNumber) + ":"+ str(length))
            if length in instancesCardsNumber:
                instancesCardsNumber.update({length:instancesCardsNumber[length]+1})
            else:
                instancesCardsNumber.update({length:1})

    print(instancesCardsNumber)

if __name__=="__main__":
    main()