from classes import *
from storyline import *
import random


def bartender_attack():
    while hp > 0 and bartender.hp > 0:
        print(f"Your HP: {hp}")
        print(f"Bartenders HP: {bartender.hp}")
        move = False
        while move == False:
            choice = int(input("1. Attack 2. Magic"))
            if choice == 1:
                print("You attack the Bartender")
                bartender.attacked()
                move = True
            if choice == 2:
                if not magic:
                    print("You havent learned any magic yet")
        if(bartender.hp > 0):
            print("The bartender takes out the colazuka and blasts you")
            bartender.attack(hp)



def troll_attack():
   while hp > 0 and troll.hp > 0:
        print(f"Your HP: {hp}")
        print(f"Troll HP: {troll.hp}")
        move = False
        while move == False:
            choice = int(input("1. Attack 2. Magic"))
            if choice == 1:
                print("You attack the Troll")
                troll.attacked()
                move = True
            if choice == 2:
                if not magic:
                    print("You havent learned any magic yet")
                else:
                    print("What magic would you like to use?")
                    if magic_num > 0:
                        print("1. Fire",end=" ")
                    if magic_num > 1:
                        print("2. Dark",end=" ")
                    if magic_num > 2:
                        print("3. Heal",end=" ")     
                    if magic_num > 3:
                        print("4. Stun",end=" ")     
                    if magic_num > 4:
                        print("5. DOOM",end="")     
                                                                                             
        if(troll.hp > 0):
            print("The Troll pulls out his pizza box and whacks you")
            troll.attack(hp)
