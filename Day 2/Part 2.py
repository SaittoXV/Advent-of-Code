import re

with open("Day 2\input.txt") as f:
    fileInput = f.read()

listInput = fileInput.split("\n")

dictItem = {"blue":"0","red":"0","green":"0"}

possibleGame = 0

for game in listInput:
    dictItem = {"blue":"0","red":"0","green":"0"}
    #print("The current game is "+game)
    currentGame = re.sub("Game [1-9][0-9]?:|Game 100:","",game)
    currentTurn = currentGame.split(";")
    for marble in currentTurn:
        #print("The current turn is "+ marble)
        color = marble.split(",")
        for marbleColor in color:
            print("The current marble: " + marbleColor)
            if marbleColor.__contains__("blue"):
                if int(marbleColor.replace("blue","")) > int(dictItem["blue"]):
                    dictItem.update({"blue" : marbleColor.replace("blue","")})
            elif marbleColor.__contains__("red"):
                if int(marbleColor.replace("red","")) > int(dictItem["red"]):
                    dictItem.update({"red": marbleColor.replace("red","")})
            else:
                if int(marbleColor.replace("green","")) > int(dictItem["green"]): 
                    dictItem.update({"green":marbleColor.replace("green","")})
            
    possibleGame = possibleGame + (int(dictItem["blue"]) * int(dictItem["green"]) * int(dictItem["red"]))
           
print("The total is "+str(possibleGame))
