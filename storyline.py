from classes import *
from actions import *

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
                change_hp(hp,-10,hp_t)
            if drink_choice == 2:
                change_hp(hp,-45,hp_t)
            if drink_choice == 3:
                change_hp(hp,-20,hp_t)
        elif mentosChoice == 2:
            print('You drink your soda. Best drink ever.')
            if drink_choice == 1:
                print('You gain 20 HP. Coke is VERY good.')
                change_hp(hp,20,hp_t)
            if drink_choice == 2:
                print('You gain like 1 HP.')
                change_hp(hp,1,hp_t)
            if drink_choice == 3:
                print('You gain 10 HP. Pretty good.')
                change_hp(hp,10,hp_t)
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
                        equip(Iron)
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
                        equip(Silver)
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
                        equip(Titanium)
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
                        equip(Gold)
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
                        equip(Diamond)
                    elif equipChoice == 2:
                        print('Nothing happens.')
                    else:
                        print('Do something.') 
                elif gold < 500:
                    print("SHOPKEEPER: Your body pillow is sad now.")
        if goodsChoice == 2:
            armor_choice = input(int("SHOPKEEPER: Are you going commando? 1: Buy leather armor, 2: Buy iron armor, 3: BUy silver armor, 4: Buy titanium armor, 5: Buy gold armor, 6: Buy diamond armor"))
            if armor_choice == 1:
                if gold 


shop()

def impDialogue():
    print("IMP: Order on the Domino's app and earn points towards free pizza!")
    pizzaChoice = int(input("Order on the Domino's App? 1: Yes, 2: No, 3: Act stupid"))
    if pizzaChoice == 1:
        eatPizza = int(input('The imp hands you his pizza. Eat some? 1: Yes, 2: No, 3: Shove it down his throat')) # If I had a nickel for every time I ate a whole pizza pie in this building, I'd have two (soon three) nickels.
        if eatPizza == 1:
            print('There are expired boogers on it and you lose 50 HP.')
            change_hp(hp,-50,hp_t)
        if eatPizza == 2:
            print('You reject the offer. Nothing happens.')
        if eatPizza == 3:
            print('The imp chokes on an anchovy and loses half HP. Your loss, bucko.')
    if pizzaChoice == 2:
        print('Nothing happens.')
    if pizzaChoice == 3:
        lunatic = int(input('You act like a deranged lunatic, causing the imp to back away. 1: Chase him, 2: Stay in place, 3: Yell stupid movie quotes'))
        if lunatic == 1:
            print('You rob the imp of his hard-earned gold. Way to go.')
            change_gold(30)
        if lunatic == 2:
            print('No one wins. No one loses. The fight ends.')
        if lunatic == 3:
            print("You scream some lines from those corny kids' movies and make a complete fool of yourself. You lose 1 HP.")
            change_hp(hp,-1,hp_t)