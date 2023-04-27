def shop():
    dialogue = int(input('Give me your wallet or get the heck out.'))
    print("1: Ask for drink, 2: Buy something else, 3: Leave")
    if dialogue == 1:
        print("SHOPKEEPER: It's like, bad for you and stuff.")
        print("1: Get Coke, 2: Get Pepsi, 3: Get Dr. Pepper")
        drink_choice = int(input('Pick a drink!'))
        if drink_choice = 1:
            print('You have Coke. DRINK!')
        if drink_choice = 2:
            print('You have Pepsi. DRINK!')
        if drink_choice = 3:
            print('You have Dr. Pepper. DRINK!')
        else:
            print('No fencesitting! DRINK!')
        mentosChoice = input('SHOPKEEP: Would you like Mentos? 1: Yes, 2: No')
        if mentosChoice = 1:
            print('The soda (along with the can) explodes in your face and amuses the shopkeeper. Oops.')
            if drink_choice == 1:
                change_hp(-10)
            if drink_choice == 2:
                change_hp(-45)
            if drink_choice == 3:
                change_hp(-20)
        elif mentosChoice = 2:
            print('You drink your soda. Best drink ever.')
            if drink_choice = 1:
                print('You gain 10 HP. Coke is VERY good.')
                change_hp(20)
            if drink_choice = 2:
                print('You gain like 1 HP.')
                change_hp(1)
        else:
            print('Stop fencesitting.')
    if dialogue == 2:
        print('SHOPKEEP: Would you like weapons or armor? 1: Get weapons, 2: Get armor')
        goodsChoice = int(input('SHOPKEEP: What are you waiting for? 1: Get weapons, 2: Get armor'))
        if goodsChoice = 1:
            print('We have swords.')
            weaponChoice = int(input('1: Iron Sword, cost 50 coins. 2: Silver Sword, cost 100 coins. 3: Titanium Sword, cost 200 coins. 4: Gold Sword, cost 350 coins. 5: Diamond Sword, cost 500 coins.'))
            if weaponChoice = 1:
                if gold >= 50:
                    print('You now have Iron Sword.')
                elif gold < 50: 
                    equipChoice = int(input('You now have Iron Sword. Equip sword? 1: Yes, 2: No'))
                    if equipChoice = 1:
                        equip(Iron)
                    if equipChoice = 2:
                        print('Nothing happens.')
                    else:
                        print('Do something.')
                    elif gold < 50: 
                        print('SHOPKEEPER: Get a job. Denied!')
                if weaponChoice = 2:
                    if gold >= 100:
                        print('You now have Silver Sword.')
                    elif gold < 50:
                        print("SHOPKEEPER: Make yourself rich so I don't have to.")
                if weaponChoice = 3:
                    if gold >= 200:
                        print('You now have Titanium Sword.')
                    elif gold < 200:
                        print("SHOPKEEPER: Why are you poor?")
                if weaponChoice = 4:
                    if gold >= 350:
                        print('You now have Gold Sword.')
                    elif gold < 350:
                        print("SHOPKEEPER: My wife pays me better.")
                if weaponChoice = 5:
                    if gold >= 500:
                        print('You now have Diamond Sword.')
                    elif gold < 500:
                        print("SHOPKEEPER: Your body pillow is sad now.")
        if goodsChoice = 2:
            print()

                