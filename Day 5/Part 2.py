import re
from collections import OrderedDict


def main():
    with open("Day 5\input.txt") as file:
        fileInput = file.read()

    fileList = fileInput.split("\n\n")

    # Get the Seed Number
    seedDict = {}
    seedLineText = fileList[0].split()

    for indexItem, item in enumerate(seedLineText):
        if item.isnumeric():
            seedDict[int(item)] = int(item)
    print("This is the seed dictionary:")
    print(seedDict)

    seedDict = rangeSeedDict(seedDict)

    # Loop File Input List
    for item in range(1, len(fileList)):
        print("The current list is ")
        print(fileList[item])
        mapList = re.sub("[a-z-A-Z]+ map:", "",
                         fileList[item]).strip().split("\n")

        seedList = []
        for line in mapList:
            value = line.split()[1]
            rangeValue = line.split()[2]
            findValue = line.split()[0]

            for dictKey, dictValue in seedDict.items():
                if dictValue >= int(value) and dictValue <= int(rangeValue)+int(value)-1 and not (dictKey in seedList):
                    print("Key " + str(dictKey))
                    print("Value " + str(dictValue))
                    foundValue = findMapping(int(dictValue), int(value),
                                             int(rangeValue), int(findValue))
                    seedDict[dictKey] = foundValue
                    seedList.append(dictKey)
                else:
                    seedDict[dictKey] = dictValue
    print("Break Point")
    print(seedDict)
    dictSorted = dict(sorted(seedDict.items(), key=lambda item: item[1]))
    print(dictSorted)


def findMapping(dictValue, value, rangeValue, findValue):

    return dictValue - (value - findValue)

    # dictMapping = {}
    # x = (i for i in range(value, rangeValue+value))
    # y = (i for i in range(findValue, rangeValue+findValue))
    # for currentX in iter(x):
    #     currentY = next(iter(y))
    #     if currentX == dictValue:
    #         dictMapping[currentX] = currentY
    #         return dictMapping[currentX]
    # print(dictMapping)


def rangeSeedDict(seedDict):
    rangeList = []
    deleteItem = []

    for indexSeed, seed in enumerate(seedDict.keys()):
        if indexSeed % 2 == 1:
            deleteItem.append(seed)

    for item in deleteItem:
        del seedDict[item]

    for indexItem, item in enumerate(seedDict.keys()):
        for i in range(item+1, deleteItem[indexItem]+item):
            rangeList.append(i)

    for item in rangeList:
        seedDict[int(item)] = int(item)

    return seedDict


if __name__ == "__main__":
    main()
