# from classes import *
# from actions import *
# from attack import * # If we test it in main we can just import everything from each file so we don't have any problems. We have no reason to import everything from each individual file
# from beemovie import *

def BarryBBenson():
    open

def shop():
    dialogue = int(input('BARTENDER: Give me your wallet or get the heck out. 1: Ask for drink, 2: Buy something else, 3: Leave, 4: Fight'))
    if dialogue == 1:
        print("BARTENDER: It's like, bad for you and stuff.")
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
        mentosChoice = int(input('BARTENDER: Would you like Mentos? 1: Yes, 2: No'))
        if mentosChoice == 1:
            print('The soda (along with the can) explodes in your face and amuses the shopkeeper. Oops.')
            if drink_choice == 1:
                print("You lose 10 HP.")
            if drink_choice == 2:
                print("You lose 45 HP.")
            if drink_choice == 3:
                print("You lose 20 HP.")
        elif mentosChoice == 2:
            print('You drink your soda. Best drink ever.')
            if drink_choice == 1:
                print('You gain 20 HP. Coke is VERY good.')
            if drink_choice == 2:
                print('You gain like 1 HP.')
            if drink_choice == 3:
                print('You gain 10 HP. Pretty good.')
                change_hp(hp,10,hp_t)
        else:
            print('Stop fencesitting.')
    if dialogue == 2:
        print('BARTENDER: Would you like weapons or armor? 1: Get weapons, 2: Get armor')
        goodsChoice = int(input('BARTENDER: What are you waiting for? 1: Get weapons, 2: Get armor'))
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
                        print('BARTENDER: Get a job. Denied!')
            if weaponChoice == 2:
                if gold >= 100:
                    equipChoice = int(input('You now have Silver Sword. Equip sword? 1: Yes, 2: No'))
                    change_gold(-100)
                    if equipChoice == 1:
                        silver.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                    elif gold < 50:
                        print("BARTENDER: Make yourself rich so I don't have to.")
                    else:
                        print("BARTENDER: Do something.")
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
                    print("BARTENDER: Why are you poor?")
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
                    print("BARTENDER: My wife pays me better.")
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
                    print("BARTENDER: Your body pillow is sad now.")
        if goodsChoice == 2:
            armor_choice = input(int("BARTENDER: Are you going commando? 1: Buy leather armor, 2: Buy iron armor, 3: Buy silver armor, 4: Buy titanium armor, 5: Buy gold armor, 6: Buy diamond armor"))
            if armor_choice == 1:
                if gold >= 100:
                    equipChoice = int(input('You now have Leather Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-100)
                    if equipChoice == 1:
                        leather.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 100:
                    print('BARTENDER: Typical.')
            if armor_choice == 2:
                if gold >= 200:
                    equipChoice = int(input('You now have Iron Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-200)
                    if equipChoice == 1:
                        iron.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 200:
                    print('BARTENDER: Stop being poor.')
            if armor_choice == 3:
                if gold >= 300:
                    equipChoice = int(input('You now have Silver Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-300)
                    if equipChoice == 1:
                        silver.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 200:
                    print('BARTENDER: Buy a silver spoon and come back.')
            if armor_choice == 4:
                if gold >= 400:
                    equipChoice = int(input('You now have Titanium Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-400)
                    if equipChoice == 1:
                        titanium.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 400:
                    print("BARTENDER: Don't wet yourself.")
            if armor_choice == 5:
                if gold >= 500:
                    equipChoice = int(input('You now have Gold Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-500)
                    if equipChoice == 1:
                        gold.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 500:
                    print("BARTENDER: Try pyrite. It fits you much better.")
            if armor_choice == 6:
                if gold >= 600:
                    equipChoice = int(input('You now have Diamond Armor. Equip armor? 1: Yes, 2: No'))
                    change_gold(-600)
                    if equipChoice == 1:
                        diamond.equip()
                    elif equipChoice == 2:
                        print('Nothing happens.')
                elif gold < 600:
                    print("BARTENDER: Shove diamonds down the toilet and see what happens.")
    if dialogue == 3:
        print('BARTENDER: Change your diaper on the way out.')
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
    boneDialogue = int(input('1: Do the Bull Charge (Mike Tysons Punch Out), 2: Eat it, 3: Ask for forbidden knowledge, 4: Fight'))
    if boneDialogue == 1:
        print('You Bull Charge your nemesis to Hell and back and earn NOTHING! You LOSE! GOOD DAY SIR!')
        return
    elif boneDialogue == 2:
        print('You choke on the bone and die in five minutes.')
    elif boneDialogue == 3:
        print('Where does he get his supply of laurels?') # In Castlevania II, some dude in Laruba Mansion gives you free laurels if you talk with him. He never exhausts his supply. Where does he get it?
        print('Before the bone responds, you are smitten by the ghost of Asa Griggs Candler. Game Over')
    elif boneDialogue == 4:
        bone.fight()

def LichDialogue():
    print("LICH: Shall I pick your nose, good sir?")
    noseChoice = int(input("1: Let him pick your nose, 2: Don't let him pick your nose, 3: Blast him with your Colazooka!"))
    if noseChoice == 1:
        print('The lich shoves a Colazooka up your nose and pulls the trigger. You are now a pile of Mentos. Game Over')
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
    wormChoice = int(input("1: 'The government is controlled by PepsiCo', 2: 'Christmas is in May,' 3: phhhhtphtphtphtphtphp"))
    if wormChoice == 1:
        print('WORM: FAKE!')
    elif wormChoice == 2: # to infinity and beyond
        print('WORM: You got that right.')
    elif wormChoice == 3:
        print('You spat on the worm. FIGHT!!')
    else:
        print("Please pick others' noses with a keyboard. DO IT!")

def medusaDialogue():
    print("MEDUSA: oh baby baby baby OOOOOHHH oh baby baby baby NOOOOOOOO")    
    medusaChoice = int(input("1: Stay and listen, 2: Fling boogers at her, 3: Sing an equally bad song"))
    if medusaChoice == 1:
        print("You turn to stone and die. GAME OVER")
    elif medusaChoice == 2:
        print("She stops and flings them back in your mouth. FIGHT!")
    elif medusaChoice == 3:
        print("Rebecca Black deserves a Colazooka up the hiney")
    else:
        print("You turn to stone for three seconds, causing your boogers to fall off and bounce to Medusa's mouth.")

def karyDialogue():
    print("KARY: I have been picking my nose for the past five hours")
    karyChoice = int(input("1: Pick its nose, 2: Punch it in the face, 3: Start a conspiracy theory, 4: Say something stupid"))
    if karyChoice == 1:
        print("Your fingers explode and become cans of Coke. GAME OVER")
    elif karyChoice == 2:
        print("OGRE FIGHT!!")
    elif karyChoice == 3: 
        print("Santa Claus is a hoax created by the government to get kids to punch people in the face.")
    elif karyChoice == 4:
        print("creating terror and government purges acting out all of your monstrous urges big brother plots that would make orwell blush these are the things that sure give me a rush spying on lenin and murdering trotsky vexing the west with his communist plotsky turning your dreams into scary nightmares that is the way i forget all my cares when the germans invade moscow and the weather's vile i simply look on as they all freeze to death and that really makes me smile feasting like ivan while serfs live in rations conquering dozens of satellite nations starting my own personality cult doing away with those who might revolt sending your critics to rot in siberia thats how you get populations to fear ya building a wall down the streets of berlin this kind of thing makes me flash quite a grin if the people call for freedom or democracy i simply bup off everybody until theres nobody left but me")
    else:
        print("You get punched in the face. WOOHOO")

def krakenDialogue():
    print("KRAKEN: i am dead") # do not try this at home
    krakenChoice = int(input("1: No you're not, 2: you are right, 3: i punched a tv in the face and got a heart attack"))
    if krakenChoice == 1:
        print("KRAKEN: PROVE IT")
        existChoice = int(input("1: the dead cannot speak"))
        if existChoice == 1:
            print("KRAKEN: ghosts speak and are dead, are you stupid?")
            ghostChoice = int(input("1: wow you're right, 2: ghosts are fake, 3: i punched a nanny in the face next five afternoons"))
            if ghostChoice == 1:
                print("KRAKEN: about you? sure, why not")
                suckChoice = int(input("Punch him in the face? 1: Yes, Anything else: No"))
                if suckChoice == 1:
                    print("FIGHT")
                else:
                    print("Your brain explodes. Kraken is right. GAME OVER") # congarlutations this story is happy end thank you you feel strongth welling in your body return to starting point challenge again
            elif ghostChoice == 2:
                print("KRAKEN: uhhhh... zombies speak and they're dead. checkmate")
                zombieChoice = int(input("1: wow you're right, 2: they're undead. thats completely different, 3: i want pizza"))
                if zombieChoice == 1:
                    print("KRAKEN: i win")
                    print("You explode because Kraken is right. GAME OVER")
                elif zombieChoice == 2:
                    print("KRAKEN: but theyre real")
                    realChoice = int(input("1: no they aren't"))
                    if realChoice == 1:
                        print("KRAKEN: whatever I'm still dead")
                        deadChoice = int(input("1: how are you speaking then"))
                        if deadChoice == 1:
                            print("Kraken is mad. FIGHT!")
                        else:
                            print("lol game over")
                elif zombieChoice == 3:
                    print("KRAKEN: come and get some!!!")
                    print("FIGHT!!")
                else:
                    print("game over lol")
            elif ghostChoice == 3:
                print("KRAKEN: what was that last part?")
                nannyChoice = int(input("1: next five afternoons, why?"))
                if nannyChoice == 1:
                    print("KRAKEN: are you on drugs???")
                    substanceChoice = int(input("1: caffeine, thank you very much"))
                    if substanceChoice == 1:
                        print("KRAKEN: you like coffee?")
                        coffeeChoice = int(input("1: yes, 2: no"))
                        if coffeeChoice == 1:
                            print("KRAKEN: huh me too... lets fight")
                        elif coffeeChoice == 2:
                            print("KRAKEN: bad for you... lets fight")
                        else:
                            print("Fencesitting is for losers. GAME OVER") 
                    else:
                        print("game over lel")
                else:
                    print("Kraken-san punches you in the face. GAME OVER")
            else:
                print("You turn into a ghost. GAME OVER")
        else:
            print("You no longer exist. GAME OVER")
    elif krakenChoice == 2:
        print("KRAKEN: ya like jazz")
        BeeMovieChoice = int(input("1: yes"))
        if BeeMovieChoice == 1:
            print("bee movie") # placeholder for the entire script
            print("FIGHT")
    elif krakenChoice == 3:
        print("KRAKEN: when are ya getting married?")
        marriageChoice = int(input("1: to whom? 2: NEVER!!!"))
        if marriageChoice == 1:
            print("KRAKEN: the tv, genius")
            tvChoice = int(input("1: no I'm a phone man!!! 2: of course"))
            if tvChoice == 1:
                print("KRAKEN: thats stupid. lets fight")
            elif tvChoice == 2:
                print("KRAKEN: alright. lets dance")
        elif marriageChoice == 2:
            print("KRAKEN: bad for you. lets fight")

def tiamatDialogue():
    print("TIAMAT: what is love?")
    loveChoice = int(input("1: baby don't hurt me, 2: i'm not your english teacher. look it up"))
    if loveChoice == 1:
        print("TIAMAT: no more...")
        nomoreChoice = int(input("1: What is love? 2: Pulverize him, 3: Stop speaking"))
        if nomoreChoice == 1:
            print("TIAMAT: you ain't never gettin' it")
            print("FIGHT!")
        elif nomoreChoice == 2:
            print("you asked for it. FIGHT!!")
        elif nomoreChoice == 3:
            print("...")
            print("TIAMAT: speak")
            speakChoice = int(input("1: Don't speak, 2: Pick your nose"))
            if speakChoice == 1:
                print("TIAMAT: lets fight. call uncle")
            elif speakChoice == 2:
                print("TIAMAT: EW what the hell?!!?! use a tissue!!!!11111!!1!one!1111!")
                snotChoice = int(input("1: Eat it, 2: Wipe it on TIAMAT, 3: Wipe it on your underwear"))
                if snotChoice == 1:
                    print("TIAMAT: THATS DISGUSTING WTF?! YOU SHALL DIE!!!!!!!!!!!!!!!!!!!!!1111111111111one")
                elif snotChoice == 2:
                    print("TIAMAT: STOP WHAT THE HELL?! GROSS IT HURTS LIKE HELL RUN AWAY RUN AWAYYYYYY")
                elif snotChoice == 3:
                    print("TIAMAT: EWWW WHAT THE HELL THATS DISGUSTING!!! DONT NEVER DO THAT AGAIN!!! EVER!!!!!!")
                print("FIGHT!!")
    if loveChoice == 2:
        print("TIAMAT: shut up")
        shutupChoice = int(input("1: takes one to know one"))
        if shutupChoice == 1:
            print("TIAMAT: speak for yourself mr. or mrs. brain damage.")

def chaosDialogue():
    print("CHAOS: are you Barry B Benson?")
    barryChoice = int(input("1: Yes, 2: No"))
    if barryChoice == 1:
        beelaw1 = str(input('CHAOS: whats bee law number 1?'))
        beelaw1.lower()
        if beelaw1 == "absolutely no talking to humans":
            print("CHAOS: man you're good.")
        else:
            print("CHAOS: THINK BEE! THINK BEE! YOU SHALL DIE")


chaosDialogue()