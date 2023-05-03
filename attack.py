from classes import *
from storyline import *
from actions import *
import random

def attack():
    random_p = power * (random.randint(1, 200)/100)
    print(f"The bartender takes {random_p} damage")
    bartender.hp -= random_p
    print(bartender.hp)

def bartender_attack():
    while hp > 0 and bartender.hp > 0:
        print(f"Your HP: {hp}")
        print(f"Bartenders HP: {bartender.hp}")
        choice = int(input("1. Attack 2. Magic"))

        if choice == 1:
            print("You attack the bartender")
            attack()