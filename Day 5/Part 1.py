import re
from collections import OrderedDict


def main():
    with open("Day 5\inputTest.txt") as file:
        fileInput = file.read()

    fileList = fileInput.split("\n\n")

    # Get the Seed Number
    seedDict = {}
    seedLineText = fileList[0].split()

    for item in seedLineText:
        if item.isnumeric():
            seedDict[int(item)] = int(item)
    print("This is the seed dictionary:")
    print(seedDict)

    # Loop File Input List
    for item in range(1, len(fileList)):
        print("The current list is ")
        print(fileList[item])
        mapList = re.sub("[a-z-A-Z]+ map:", "",
                         fileList[item]).strip().split("\n")

        for line in mapList:
            value = line.split()[1]
            rangeValue = line.split()[2]
            findValue = line.split()[0]

            for dictKey, dictValue in seedDict.items():
                if dictValue >= int(value) and dictValue <= int(rangeValue)+int(value)-1:
                    print("The current dictionary value is ")
                    print(dictValue)
                    foundValue = findMapping(int(dictValue), int(value),
                                             int(rangeValue), int(findValue))
                    seedDict[dictKey] = foundValue
                else:
                    seedDict[dictKey] = dictValue
        print("Break Point")


def findMapping(dictValue, value, rangeValue, findValue):
    dictMapping = {}
    findValue = findValue - 1
    rangeValue = rangeValue + value
    for currentValue in range(value, rangeValue):
        dictMapping[currentValue] = findValue + 1
        findValue = findValue + 1
    print(dictMapping)
    for item in dictMapping.keys():
        if item == dictValue:
            return dictMapping[item]


if __name__ == "__main__":
    main()
