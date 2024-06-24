import re

with open("Day 2\input.txt") as f:
    fileInput = f.read()

listInput = fileInput.split("\n")

dictItem = {"blue":"0","red":"0","green":"0"}

possibleGame = 5050

for game in listInput:
    dictItem = {"blue":"0","red":"0","green":"0"}
    #print("The current game is "+game)
    currentGame = re.sub("Game [1-9][0-9]?:|Game 100:","",game)
    currentTurn = currentGame.split(";")
    for marble in currentTurn:
        #print("The current turn is "+ marble)
        color = marble.split(",")
        for marbleColor in color:
            #print("The current marble: " + marbleColor)
            if marbleColor.__contains__("blue"):
                dictItem.update({"blue" : marbleColor.replace("blue","")})
            elif marbleColor.__contains__("red"):
                dictItem.update({"red": marbleColor.replace("red","")})
            else:
                dictItem.update({"green":marbleColor.replace("green","")})
            
        if int(dictItem["red"]) > 12 or int(dictItem["blue"]) > 14 or int(dictItem["green"]) > 13:
            temp = game.replace(currentGame,"")
            print("Not applicable - " + temp)
            temp = temp.replace("Game","")
            temp = temp.replace(":","")
            temp.strip
            possibleGame = possibleGame - int(temp)
            break

           
print("The total is "+str(possibleGame))
