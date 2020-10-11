import random
import sys
import json

choice = ""
rooms = json.loads(open('rooms.json').read())




def AU() :
    #AU() START
    print("What map do you want to learn? The_Skeld / Polus / MIRA_HQ  other commands map_links / Exit  (remember this is case sensitive)")
    cmd = input("")
    mapChosen = cmd

    if cmds == "Change_Map" or cmd == "Exit" or cmd == "map_links" :
        cmds(cmd)

    elif cmd == "The_Skeld" or cmd == "Polus" or cmd == "MIRA_HQ" :
        cmds2(mapChosen)
    #AU() END



def cmds(cmd) :

    if cmd == "Change_Map":
        AU()

    elif cmd == "Exit":
        sys.exit()

    elif cmd == "map_links":

        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("The Skeld: https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4f/SKELD_MAP.jpg/revision/latest?cb=20200914210838")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("Polus: https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4c/Polus.png/revision/latest?cb=20200907133344")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("MIRA HQ: https://vignette.wikia.nocookie.net/among-us-wiki/images/0/0a/Mirahq.png/revision/latest?cb=20200907132939")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        AU()



def cmds2(mapChosen) :

    if mapChosen == "The_Skeld":
            
        num = random.randrange(0, 13)
        print("------")
        print("go to: ", rooms[num])
        print("------")

    elif mapChosen == "Polus" :

        num = random.randrange(14, 29)
        print("------")
        print("go to: ", rooms[num])
        print("------")

    elif mapChosen == "MIRA_HQ":

        num = random.randrange(29, 41)
        print("------")
        print("go to: ", rooms[num])
        print("------")

    input("Press enter to go to the next room")
    cmds2(mapChosen)

AU()