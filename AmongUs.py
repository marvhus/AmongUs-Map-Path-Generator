import random
import sys
import json
import os

rooms = json.loads(open('rooms.json').read())

line = "--------------------"

def AU() :
    #AU() START
    print(line)
    print("What map do you want to learn? The_Skeld / Polus / MIRA_HQ")
    print("other commands: maps / Exit  (remember this is case sensitive)")
    print(line)
    cmd = input("")
    mapChosen = cmd

    if cmds == "Change_Map" or cmd == "Exit" or cmd == "maps" :
        cmds(cmd)

    elif cmd == "The_Skeld" or cmd == "Polus" or cmd == "MIRA_HQ" :
        cmds2(mapChosen)

    


    #AU() END

def cmds(cmd) :

    if cmd == "Change_Map":
        AU()

    elif cmd == "Exit":
        sys.exit()

    elif cmd == "maps":

        print(line)
        print("In the images folder find the map for the map you are playing")
        print(line)
        print("Press enter to continue")
        input()
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
   

    print("Press enter to go to the next room")
    input()
    cmds2(mapChosen)

AU()