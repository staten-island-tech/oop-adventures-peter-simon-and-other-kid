from classes import *
from storyline import *

import random


def bartender_attack():
    while hp > 0 and bartender.hp > 0:
        output(f"Your HP: {hp}")
        output(f"Bartenders HP: {bartender.hp}")
        move = False
        while move == False:
            choice = int(input("1. Attack 2. Magic"))
            if choice == 1:
                output("You attack the Bartender")
                bartender.attacked()
                move = True
            if choice == 2:
                if not magic:
                    output("You havent learned any magic yet")
        if(bartender.hp > 0):
            output("The bartender takes out the colazuka and blasts you")
            bartender.attack(hp)



def troll_attack():
   while hp > 0 and troll.hp > 0:
        output(f"Your HP: {hp}")
        output(f"Troll HP: {troll.hp}")
        move = False
        while move == False:
            choice = int(input("1. Attack 2. Magic"))
            if choice == 1:
                output("You attack the Troll")
                troll.attacked()
                move = True
            if choice == 2:
                if magic_num < 1:
                    output("You havent learned any magic yet")
                else:
                    if magic_num > 0:
                        print("1. Fire",end=" ")
                    if magic_num > 1:
                        print("2. Dark",end=" ")
                    if magic_num > 2:
                        print("3. Heal",end="")     
                    if magic_num > 3:
                        print("4. Stun",end=" ")     
                    if magic_num > 4:
                        print("5. DOOM",end="")    
                    magic_choice = int(input(("What magic would you like to use?")))
                if magic_choice <= magic_num and magic_choice > 0:
                    if magic_choice == 3:
                        heal = (20 + random.randint(1,10))
                        hp += heal
                        output(f"You gained {heal} hp")
                    else: 
                        troll.magic(magic_num)
                                                                                             
        if(troll.hp > 0 and troll.check_stun() == False):
            output("The Troll pulls out his pizza box and whacks you")
            troll.attack(hp)
