import re

with open("Day 3\inputTest.txt") as f:
    fileInput = f.read()

totalValue = 0

fileInput = fileInput.replace("."," ")
fileInput = re.sub("[*#+$/=&!@%^()-]","-",fileInput) 
# [0-9]|[*#+$/=&!@%^()-]


for countList, value in enumerate(fileInput.split("\n")):
    print(value + " -> " +  str(countList))
    tempList = re.findall("[0-9]+",value)
    for countNumber, item in enumerate(tempList):
        dictIndexNumber =  {}
        dictIndexNumber.update({"end":value.index(item)+len(item)})
        dictIndexNumber.update({"start":value.index(item)})
        for number in range(dictIndexNumber["start"],dictIndexNumber["end"],1):
            print(value[number])
            nextItem = countList + 1
            beforeItem = countList - 1
            try:
                if countList > 0:
                    if (fileInput.split("\n")[beforeItem][number] == "-" or 
                        fileInput.split("\n")[beforeItem][number+1] == "-" or 
                        fileInput.split("\n")[beforeItem][number-1] == "-" or 
                        fileInput.split("\n")[countList][number+1] == "-"):
                            totalValue += int(item)
                            break
                if (fileInput.split("\n")[nextItem][number] == "-" or 
                    fileInput.split("\n")[nextItem][number+1] == "-" or 
                    fileInput.split("\n")[nextItem][number-1] == "-" or 
                    fileInput.split("\n")[countList][number+1] == "-"):
                        totalValue += int(item)
                        break
            except:
                print("List out of range")
print("the total value is "+str(totalValue))

# if fileInput.split("\n")[countList][countString] == " " or value[countString+1] == " ":