from classes import *
from actions import *
from attack import * # If we test it in main we can just import everything from each file so we don't have any problems.

def shop():
    dialogue = int(input('Give me your wallet or get the heck out. 1: Ask for drink, 2: Buy something else, 3: Leave, 4: Fight'))
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
                    change_gold(-50)
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
                    change_gold(-100)
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
                    change_gold(-200)
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
                    change_gold(-350)
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
                    change_gold(-500)
                    if equipChoice == 1:
                        diamond.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                    else:
                        print('Do something.') 
                elif gold < 500:
                    print("SHOPKEEPER: Your body pillow is sad now.")
        if goodsChoice == 2:
            armor_choice = input(int("SHOPKEEPER: Are you going commando? 1: Buy leather armor, 2: Buy iron armor, 3: Buy silver armor, 4: Buy titanium armor, 5: Buy gold armor, 6: Buy diamond armor"))
            if armor_choice == 1:
                if gold >= 100:
                    equipChoice = int(input('You now have Leather Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-100)
                    if equipChoice == 1:
                        leather.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 100:
                    print('SHOPKEEPER: Typical.')
            if armor_choice == 2:
                if gold >= 200:
                    equipChoice = int(input('You now have Iron Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-200)
                    if equipChoice == 1:
                        iron.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 200:
                    print('SHOPKEEPER: Stop being poor.')
            if armor_choice == 3:
                if gold >= 300:
                    equipChoice = int(input('You now have Silver Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-300)
                    if equipChoice == 1:
                        silver.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 200:
                    print('SHOPKEEPER: Buy a silver spoon and come back.')
            if armor_choice == 4:
                if gold >= 400:
                    equipChoice = int(input('You now have Titanium Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-400)
                    if equipChoice == 1:
                        titanium.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 400:
                    print("SHOPKEEPER: Don't wet yourself.")
            if armor_choice == 5:
                if gold >= 500:
                    equipChoice = int(input('You now have Gold Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-500)
                    if equipChoice == 1:
                        gold.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 500:
                    print("SHOPKEEPER: Try pyrite. It's much better for you.")
            if armor_choice == 6:
                if gold >= 600:
                    equipChoice = int(input('You now have Diamond Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-600)
                    if equipChoice == 1:
                        diamond.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 600:
                    print("SHOPKEEPER: Shove diamonds down the toilet and see what happens.")
    if dialogue == 3:
        print('SHOPKEEPER: Change your diaper on the way out.')
        return
    if dialogue == 4:
        bartender_attack()

# shop()

def impDialogue():
    print("IMP: Order on the Domino's app and earn points towards free pizza!")
    pizzaChoice = int(input("Order on the Domino's App? 1: Yes, 2: No, 3: Act stupid"))
    if pizzaChoice == 1:
        eatPizza = int(input('The imp hands you his pizza. Eat some? 1: Yes, 2: No, 3: Shove it down his throat')) # If I had a nickel for every time I ate a whole pizza pie in this building, I'd have three nickels.
        if eatPizza == 1:
            print('There are expired boogers on it and you lose 50 HP.')
            change_hp(hp,-50,hp_t)
        elif eatPizza == 2:
            print('You reject the offer. Nothing happens.')
        elif eatPizza == 3:
            print('The imp chokes on an anchovy and loses half HP. Your loss, bucko.')
        else:
            print('You do nothing. The imp shoves it in his mouth and calls it a day.')
    if pizzaChoice == 2:
        print('Nothing happens.')
    if pizzaChoice == 3:
        lunatic = int(input('You act like a deranged lunatic, causing the imp to back away. 1: Chase him, 2: Stay in place, 3: Yell stupid movie quotes'))
        if lunatic == 1:
            print('You rob the imp of his hard-earned gold. Way to go.')
            change_gold(30)
        elif lunatic == 2:
            print('No one wins. No one loses. The fight ends.')
        elif lunatic == 3:
            print("You scream some lines from those corny kids' movies and make a complete fool of yourself. The imp gets away and you lose 1 HP.")
            change_hp(hp,-1,hp_t)
        else:
            print('The imp stops running and pummels you with the pizza box. You lose 20 HP.')
            change_hp(hp,-20,hp_t)
            return

def trollDialogue():
    print("TROLL: U MAD BRO?")
    dialogueChoice = int(input('1: Stare in confusion, 2: Pound his face in, 3: Recite the Bee Movie script, 4: Megaman 8, 5: Do a backflip, Anything else: Run away'))
    if dialogueChoice == 1:
        print('TROLL: The FitnessGram pacer test is a multistage aerobic capacity test. It will...')
        print('Five hours later...')
        print('TROLL: On your mark. Get ready. Start.')
    elif dialogueChoice == 2:
        troll.attack()
    elif dialogueChoice == 3:
        print("According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible...")
        print('Ten hours later...')
        print("We live on two cups a year. They put it in lip balm for no reason whatsoever...")
        print('Five more hours later...')
        print("Wrap it up, guys. I had virtually no rehearsal for that.")
        print('Troll: OH MY GOD')
        print('The troll escapes.')
    elif dialogueChoice == 4:
        print("mega man today we finnish this hay bass wy must i fight you wii are not enemys shut up aaaaauuuugh mega maaaaan roll mega man you must come with me you cant leave yet uh aaaaaaugh rush jet wooooooo bass we have to do thi s some ofer time aaauuuuugh run away cowerd yull pay for this insult ill be back")
        print('The troll stares in disbelief.')
    elif dialogueChoice == 5:
        print("You trip over a pebble and break your neck. GAME OVER")
        change_hp(hp,100,hp_t)
    else:
        print('RUN AWAY RUN AWAAAAYYYYYY')
        return


def WolfDialogue():
    print("WOLF: EAT MY CHILI")
    dialogueChoice = int(input("1: Eat the chili, 2: Don't eat the chili, 3: Shove it in the wolf's face"))
    if dialogueChoice == 1:
        print("Your stomach explodes. Taco Bell move. You lose 99 HP.")
        change_hp(hp,100,hp_t)
    if dialogueChoice == 2:
        print('Nothing happens and the wolf is disgruntled. FIGHT!!')
        wolf.attack()
    if dialogueChoice == 3:
        print("You stuff the wolf's face with chili. It explodes in his face. Run away?")
        runChoice = int(input("1: Run away, 2: Don't run away"))
        if runChoice == 1:
            print('RUN AWAY RUN AWAAAAYYYYYY')
            return
        if runChoice == 2:
            print('FIGHT!!!')
            wolf.attack()
        else:
            wolf.attack()
    else:
        print("You explode. Oops.")
        change_hp(hp,-100,hp_t)
        return
    
def BoneDialogue():
    print("BONE: [unfunny skeleton-related quip here]")
    boneDialogue = int(input('1: Do the Bull Charge, 2: Eat it, 3: Ask for forbidden knowledge, 4: Fight'))
    if boneDialogue == 1:
        print('You Bull Charge your nemesis to Hell and back and earn NOTHING! You LOSE! GOOD DAY SIR!')
        return
    elif boneDialogue == 2:
        print('You choke on the bone and die in five minutes.')
    elif boneDialogue == 3:
        print('Where does he get his supply of laurels?') # In Castlevania II, there's this guy in Laruba Mansion's basement who gives you free laurels. He never exhausts his supply. Where does he get it?
        print('Before the bone responds, you are smitten by the ghost of Asa Griggs Candler. Game Over')
    elif boneDialogue == 4:
        bone.fight()

def LichDialogue():
    print("LICH: Shall I pick your nose, good sir?")
    noseChoice = int(input("1: Let him pick your nose, 2: Don't let him pick your nose, 3: Blast him with your Colazooka!"))
    if noseChoice == 1:
        print('The lich shoves the Colazooka up your nose and pulls the trigger. You are now a pile of Mentos. Game Over')
    elif noseChoice == 2:
        print('Nothing happens. You fight anyway.')
    elif noseChoice == 3:
        print('The lich snatches it from you before you can use it. He pulls the trigger and you explode. GAME OVER')
    else:
        print('The lich punches you into space for being a fencesitter. Game Over')

def WizardDialogue():
    print("WIZARD: uhuhuhuh... kids shows funny... uhhuhuhh...")
    wizardChoice = int(input("1: Kick 'it' to him, 2: Ask for his age, 3: Pick your nose, 4: Ask for his weight"))
    if wizardChoice == 1:
        print('WIZARD picks his nose all the time. FIGHT!')
    elif wizardChoice == 2:
        print("me 31 years old lel") # prime number
    elif wizardChoice == 3:
        print("Before you can eat it, the wizard slaps your boogers out of your hand and challenges you to a duel. FIGHT!")
    elif wizardChoice == 4:
        print("The wizard tips over and crushes you with his immense weight. GAME OVER")
    else:
        print("The wizard picks his nose and has you eat it. Nothing happens.")

def wormDialogue():
    print("WORM: jfjiefjiwejwfjiweef")
    wormChoice = int(input("1: 'The government is controlled by PepsiCo', 2: 'Christmas is in May,' 3: "))
    


shop()
impDialogue()
trollDialogue()
WolfDialogue()
BoneDialogue()