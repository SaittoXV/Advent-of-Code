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

            for dictValue in seedDict.values():
                if dictValue >= int(value) and dictValue <= int(rangeValue)+int(value):
                    print(dictValue)
                    findMapping()


def findMapping():
    print("In Range")


if __name__ == "__main__":
    main()
