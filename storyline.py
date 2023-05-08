from classes import *
from actions import *
from attack import *

magic_num = 0
def shop():
    dialogue = int(input('Give me your wallet or get the heck out. 1: Ask for drink, 2: Buy something else, 3: Leave'))
    if dialogue == 1:
        print("SHOPKEEPER: It's like, bad for you and stuff.")
        drink_choice = int(input("1: Get Coke, 2: Get Pepsi, 3: Get Dr. Pepper"))
        while drink_choice > 3:
            print('No fencesitting! DRINK!')
            drink_choice = int(input("1: Coke, 2: Pepsi, 3: Dr Pepper. DRINK!"))
            if drink_choice < 3:
                break
        if drink_choice == 1:
            print('You have Coke. DRINK!')
        if drink_choice == 2:
            print('You have Pepsi. DRINK!')
        if drink_choice == 3:
            print('You have Dr. Pepper. DRINK!')
        mentosChoice = int(input('SHOPKEEP: Would you like Mentos? 1: Yes, 2: No'))
        if mentosChoice == 1:
            print('The soda (along with the can) explodes in your face and amuses the shopkeeper. Oops.')
            if drink_choice == 1:
                change_hp(-10)
            if drink_choice == 2:
                change_hp(-45)
            if drink_choice == 3:
                change_hp(-20)
        elif mentosChoice == 2:
            print('You drink your soda. Best drink ever.')
            if drink_choice == 1:
                print('You gain 20 HP. Coke is VERY good.')
                change_hp(20)
            if drink_choice == 2:
                print('You gain like 1 HP.')
                change_hp(1)
            if drink_choice == 3:
                print('You gain 10 HP. Pretty good.')
                change_hp(10)
        else:
            print('Stop fencesitting.')
    if dialogue == 2:
        print('SHOPKEEP: Would you like weapons or armor? 1: Get weapons, 2: Get armor')
        goodsChoice = int(input('SHOPKEEP: What are you waiting for? 1: Get weapons, 2: Get armor'))
        if goodsChoice == 1:
            print('We have swords.')
            weaponChoice = int(input('1: Iron Sword, cost 50 coins. 2: Silver Sword, cost 100 coins. 3: Titanium Sword, cost 200 coins. 4: Gold Sword, cost 350 coins. 5: Diamond Sword, cost 500 coins.'))
            if weaponChoice == 1:
                if gold >= 50:
                    equipChoice = int(input('You now have Iron Sword. Equip sword? 1: Yes, 2: No'))
                    if equipChoice == 1:
                        iron.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                    else:
                        print('Do something.')                    
                elif gold < 50: 
                        print('SHOPKEEPER: Get a job. Denied!')
            if weaponChoice == 2:
                if gold >= 100:
                    equipChoice = int(input('You now have Silver Sword. Equip sword? 1: Yes, 2: No'))
                    if equipChoice == 1:
                        silver.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                    elif gold < 50:
                        print("SHOPKEEPER: Make yourself rich so I don't have to.")
                    else:
                        print("SHOPKEEPER: Do something.")
            if weaponChoice == 3:
                if gold >= 200:
                    equipChoice = int(input('You now have Titanium Sword. Equip sword? 1: Yes, 2: No'))
                    if equipChoice == 1:
                        titanium.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                    else:
                        print('Do something.') 
                elif gold < 200:
                    print("SHOPKEEPER: Why are you poor?")
            if weaponChoice == 4:
                if gold >= 350:
                    equipChoice = int(input('You now have Gold Sword. Equip sword? 1: Yes, 2: No'))
                    if equipChoice == 1:
                        gold.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                    else:
                        print('Do something.') 
                elif gold < 350:
                    print("SHOPKEEPER: My wife can do better.")
            if weaponChoice == 5:
                if gold >= 500:
                    equipChoice = int(input('You now have Diamond Sword. Equip sword? 1: Yes, 2: No'))
                    if equipChoice == 1:
                        diamond.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                    else:
                        print('Do something.') 
                elif gold < 500:
                    print("SHOPKEEPER: Your body pillow is sad now.")
        if goodsChoice == 2:
            print()

shop()

def impDialogue():
    print("Order on the Domino's app and earn points towards free pizza!")
    pizzaChoice = int(input("Order on the Domino's App? 1: Yes, 2: No, 3: Act stupid"))
    if pizzaChoice == 1:
        eatPizza = int(input('The imp hands you his pizza. Eat some? 1: Yes, 2: No, 3: Shove it down his throat')) # If I had a nickel for every time I ate a whole pizza pie in this building, I'd have two (soon three) nickels.
        if eatPizza == 1:
            print('There are expired booges on it and you lose 50 HP.')
            change_hp(-50)
        if eatPizza == 2:
            print('You reject the offer. Nothing happens.')
        if eatPizza == 3:
            print('')