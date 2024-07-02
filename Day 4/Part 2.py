import re
with open("Day 4\inputTest.txt") as file:
    inputFile = file.readlines()

instancesCardsNumber = {}

def main():
    for indexRow, row in enumerate(inputFile):
        matchCase = []
        cardNumber = re.findall("Card\s+[0-9]+",row)
        cardNumber = str(cardNumber[0])
        cardNumber = cardNumber.replace("Card","").strip()
        currentRow = re.sub("Card\s+[0-9]+:","",row).strip()
        partOne = currentRow.split("|")[0]
        partOne = partOne.strip().split()
        partTwo = currentRow.split("|")[1]
        partTwo = partTwo.strip().split()
        if cardNumber in instancesCardsNumber:
            instancesCardsNumber.update({cardNumber:instancesCardsNumber[cardNumber]+1})
        else:
            instancesCardsNumber.update({cardNumber:1})

        for indexColumn, column in enumerate(partOne):
            for columnPartTwo in partTwo:
                if str(partOne[indexColumn]).strip() == str(columnPartTwo).strip():
                    matchCase.append(columnPartTwo)
        for length in range(int(cardNumber) + 1,len(matchCase) + int(cardNumber) + 1):
             if str(length) in instancesCardsNumber:
                instancesCardsNumber.update({str(length):instancesCardsNumber[str(length)]+instancesCardsNumber[str(indexRow)]})
                print(instancesCardsNumber)
             else:
                instancesCardsNumber.update({str(length):1})
                print(instancesCardsNumber)

if __name__=="__main__":
    main()
    print("The Instances of All Card is " + str(instancesCardsNumber))
    print(sum(instancesCardsNumber.values()))



       
