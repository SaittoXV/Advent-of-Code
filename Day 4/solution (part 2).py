matchItem = {}

with open("Day 4\inputTest.txt") as file:
    inputFile = file.readlines()

for indexRow, row in enumerate(inputFile):
    if indexRow not in matchItem:
        matchItem[indexRow] = 1
    
    row = row.split(":")[1].strip()
    cardOne, cardTwo = [list(map(int,card.split())) for card in row.split(" | ")]
    sumSimilar = sum(item in cardOne for item in cardTwo)
    print("The sum is "+str(sumSimilar))

    for item in range(indexRow+1, indexRow+sumSimilar+1):
        matchItem[item] = matchItem.get(item,1) + matchItem[indexRow]
        print("The Current Match Item is "+str(item) + " " +str(matchItem[item]))
print(matchItem)
print(sum(matchItem.values()))