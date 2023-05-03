from classes import *
#from storyline import *
from actions import *
import random


def bartender_attack():
    while hp > 0 and bartender.hp > 0:
        print(f"Your HP: {hp}")
        print(f"Bartenders HP: {bartender.hp}")
        choice = int(input("1. Attack 2. Magic"))

        if choice == 1:
            print("You attack the Bartender")
            bartender.attack()




bartender_attack()