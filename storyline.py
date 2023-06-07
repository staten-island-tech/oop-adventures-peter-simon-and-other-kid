# from classes import *
# from actions import *
# from attack import * # If we test it in main we can just import everything from each file so we don't have any problems. We have no reason to import everything from each individual file
# from beemovie import *

from actions import change_hp, change_gold, hp, hp_t, gold # comma
# from classes import monsters
# from classes import bartender, troll, wolf, bone, lich, wizard, worm, medusa, kary, kraken, tiamat, chaos

class storyline:
    def shop():
        dialogue = 5
        while dialogue > 4 or dialogue < 1:
            dialogue = int(input('BARTENDER: Give me your wallet or get the heck out. 1: Ask for drink, 2: Buy something else, 3: Leave, 4: Fight'))
        if dialogue == 1:
            print("BARTENDER: It's like, bad for you and stuff.")
            drink_choice = int(input("1: Get Coke, 2: Get Pepsi, 3: Get Dr. Pepper"))
            while drink_choice > 3 or drink_choice < 1:
                print('No fencesitting! DRINK!')
                drink_choice = int(input("1: Coke, 2: Pepsi, 3: Dr Pepper. DRINK!"))
            if drink_choice == 1:
                print('You have Coke. DRINK!')
            elif drink_choice == 2:
                print('You have Pepsi. DRINK!')
            elif drink_choice == 3:
                print('You have Dr. Pepper. DRINK!')
            mentosChoice = 3
            while mentosChoice < 1 or mentosChoice > 2:
                mentosChoice = int(input('BARTENDER: Would you like Mentos? 1: Yes, 2: No'))
            if mentosChoice == 1:
                print('The soda (along with the can) explodes in your face and amuses the shopkeeper. Oops.')
                if drink_choice == 1:
                    print("You lose 10 HP.")
                    change_hp(hp,-10,hp_t)
                elif drink_choice == 2:
                    print("You lose 45 HP.")
                    change_hp(hp,-45,hp_t)
                elif drink_choice == 3:
                    print("You lose 20 HP.")
                    change_hp(hp,-20,hp_t)
            elif mentosChoice == 2:
                print('You drink your soda. Best drink ever.')
                if drink_choice == 1:
                    print('You gain 20 HP. Coke is VERY good.')
                    change_hp(hp,20,hp_t)
                elif drink_choice == 2:
                    print('You gain like 1 HP.')
                    change_hp(hp,1,hp_t)
                elif drink_choice == 3:
                    print('You gain 10 HP. Pretty good.')
                    change_hp(hp,10,hp_t)
        elif dialogue == 2:
            print('BARTENDER: Would you like weapons or armor? 1: Get weapons, 2: Get armor')
            goodsChoice = 3
            while goodsChoice > 2 or goodsChoice < 1:
                goodsChoice = int(input('BARTENDER: What are you waiting for? 1: Get weapons, 2: Get armor'))
            if goodsChoice == 1:
                print('We have swords.')
                weaponChoice = 6
                while weaponChoice < 1 or weaponChoice > 5:
                    weaponChoice = int(input('1: Iron Sword, cost 50 coins. 2: Silver Sword, cost 100 coins. 3: Titanium Sword, cost 200 coins. 4: Gold Sword, cost 350 coins. 5: Diamond Sword, cost 500 coins.'))
                if weaponChoice == 1:
                    if gold >= 50:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Iron Sword. Equip sword? 1: Yes, 2: No'))
                        change_gold(-50)
                        if equipChoice == 1:
                            # iron.equip() Revert these lines to actual code once I import them (ctrl+/)
                            print("BARTENDER: Congrats. Now go home and cry yourself to sleep.")
                        elif equipChoice == 2:
                            print('Nothing happens.')                   
                    elif gold < 50: 
                            print('BARTENDER: Get a job. Denied!')
                elif weaponChoice == 2:
                    if gold >= 100:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Silver Sword. Equip sword? 1: Yes, 2: No'))
                        change_gold(-100)
                        if equipChoice == 1:
                            # silver.equip() 
                            print("congralutation")
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 100:
                        print("BARTENDER: Make yourself rich so I don't have to.")
                elif weaponChoice == 3:
                    if gold >= 200:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Titanium Sword. Equip sword? 1: Yes, 2: No'))
                        change_gold(-200)
                        if equipChoice == 1:
                            # titanium.equip()
                            print("congratulations")
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 200:
                        print("BARTENDER: Why are you poor?")
                elif weaponChoice == 4:
                    if gold >= 350:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Gold Sword. Equip sword? 1: Yes, 2: No'))
                        change_gold(-350)
                        if equipChoice == 1:
                            # gold.equip()
                            print("poopy")
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 350:
                        print("BARTENDER: My wife pays me better.")
                elif weaponChoice == 5:
                    if gold >= 500:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Diamond Sword. Equip sword? 1: Yes, 2: No'))
                        change_gold(-500)
                        if equipChoice == 1:
                            # diamond.equip()
                            print("you now prossess diamond... whatever... dairy queen...") # they have the best shakes
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 500:
                        print("BARTENDER: Your body pillow is sad now.")
            elif goodsChoice == 2:
                armor_choice = 7
                equipChoice = 3
                while armor_choice > 6 or armor_choice < 1:
                    armor_choice = int(input("BARTENDER: Are you going commando? 1: Buy leather armor, 2: Buy iron armor, 3: Buy silver armor, 4: Buy titanium armor, 5: Buy gold armor, 6: Buy diamond armor"))
                if armor_choice == 1:
                    if gold >= 100:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Leather Armor. Equip armor? 1: Yes, 2: No'))
                        change_gold(-100)
                        if equipChoice == 1:
                            # leather.equip()
                            print("comment 139 if you like dairy queen")
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 100:
                        print('BARTENDER: Typical.')
                elif armor_choice == 2:
                    if gold >= 200:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Iron Armor. Equip armor? 1: Yes, 2: No'))
                        change_gold(-200)
                        if equipChoice == 1:
                            # iron.equip()
                            print("mcdonalds")
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 200:
                        print('BARTENDER: Stop being poor.')
                elif armor_choice == 3:
                    if gold >= 300:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Silver Armor. Equip armor? 1: Yes, 2: No'))
                        change_gold(-300)
                        if equipChoice == 1:
                            # silver.equip()
                            print("ag")
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 200:
                        print('BARTENDER: Buy a silver spoon and come back.')
                elif armor_choice == 4:
                    if gold >= 400:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Titanium Armor. Equip armor? 1: Yes, 2: No'))
                        change_gold(-400)
                        if equipChoice == 1:
                            # titanium.equip()
                            print("a squared = b squared + c squared - 2 bc cos a")
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 400:
                        print("BARTENDER: Don't wet yourself.")
                elif armor_choice == 5:
                    if gold >= 500:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Gold Armor. Equip armor? 1: Yes, 2: No'))
                        change_gold(-500)
                        if equipChoice == 1:
                            # gold.equip()
                            print("by the power vested in me i sentence the inventor of clamshell packaging to PRISON for one billion years")
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 500:
                        print("BARTENDER: Try pyrite. It fits you much better.")
                elif armor_choice == 6:
                    if gold >= 600:
                        equipChoice = 3
                        while equipChoice > 2 or equipChoice < 1:
                            equipChoice = int(input('You now have Diamond Armor. Equip armor? 1: Yes, 2: No'))
                        change_gold(-600)
                        if equipChoice == 1:
                            # diamond.equip()
                            print("one hundred thousand")
                        elif equipChoice == 2:
                            print('Nothing happens.')
                    elif gold < 600:
                        print("BARTENDER: Shove diamonds down the toilet and see what happens.")
        elif dialogue == 3:
            print('BARTENDER: Change your diaper on the way out.')
            return
        elif dialogue == 4:
            # bartender.attack()
            print("FIGH- wait where're you going")

    shop()

    def impDialogue():
        print("IMP: Order on the Domino's app and earn points towards free pizza!")
        pizzaChoice = 4
        while pizzaChoice > 3 or pizzaChoice < 1:
            pizzaChoice = int(input("Order on the Domino's App? 1: Yes, 2: No, 3: Act stupid"))
        if pizzaChoice == 1:
            eatPizza = 4
            while eatPizza > 3 or eatPizza < 1:
                eatPizza = int(input('The imp hands you his pizza. Eat some? 1: Yes, 2: No, 3: Shove it down his throat')) # If I had a nickel for every time I ate a whole pizza pie in this building, I'd have four (soon five!!) nickels.
            if eatPizza == 1:
                print('There are expired boogers on it and you lose 50 HP.')
                change_hp(hp,-50,hp_t)
            elif eatPizza == 2:
                print('You reject the offer. Nothing happens.')
            elif eatPizza == 3:
                print('The imp chokes on an anchovy and loses half HP. Your loss, bucko.')
        elif pizzaChoice == 2:
            print('Nothing happens.')
        elif pizzaChoice == 3:
            lunatic = 4
            while lunatic > 3 and lunatic < 1:
                lunatic = int(input('You act like a deranged lunatic, causing the imp to back away. 1: Chase him, 2: Stay in place, 3: Yell stupid movie quotes'))
            if lunatic == 1:
                print('You rob the imp of his hard-earned gold. Way to go.')
                change_gold(30)
            elif lunatic == 2:
                print('No one wins. No one loses. The fight ends.')
            elif lunatic == 3:
                print("You scream some lines from those corny kids' movies and make a complete fool of yourself. The imp gets away and you lose 1 HP.")
                change_hp(hp,-1,hp_t)

    def trollDialogue():
        print("TROLL: U MAD BRO?")
        dialogueChoice = 6
        while dialogueChoice > 5 or dialogueChoice < 1:
            dialogueChoice = int(input('1: Stare in confusion, 2: Pound his face in, 3: Recite the Bee Movie script, 4: ???, 5: Do a backflip, Anything else: Run away'))
        if dialogueChoice == 1:
            print('TROLL: The FitnessGram pacer test is a multistage aerobic capacity test. It will...')
            print('Five hours later...')
            print('TROLL: On your mark. Get ready. Start.')
        elif dialogueChoice == 2:
            print("fight mike tyson")
            # troll.attack()
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
            print("You trip over a pebble and break your neck.")
            change_hp(hp,-1,hp_t) 
            return


    def WolfDialogue():
        print("WOLF: EAT MY CHILI")
        dialogueChoice = 4
        while dialogueChoice > 3 or dialogueChoice < 1:
            dialogueChoice = int(input("1: Eat the chili, 2: Don't eat the chili, 3: Shove it in the wolf's face"))
        if dialogueChoice == 1:
            print("Your stomach explodes. Taco Bell move. You lose 99 HP.")
            change_hp(hp,-99,hp_t)
        elif dialogueChoice == 2:
            print('Nothing happens and the wolf is disgruntled. FIGHT!!')
            # wolf.attack()
        elif dialogueChoice == 3:
            print("You stuff the wolf's face with chili. It explodes in his face. Run away?")
            runChoice = 3
            while runChoice > 2 or runChoice < 1:
                runChoice = int(input("1: Run away, 2: Don't run away"))
            if runChoice == 1:
                print('RUN AWAY RUN AWAAAAYYYYYY')
                return
            elif runChoice == 2:
                print('FIGHT!!!')
                # wolf.attack()
        
    def BoneDialogue():
        print("BONE: [unfunny skeleton-related quip here]")
        boneDialogue = 5
        while boneDialogue > 4 or boneDialogue < 1:
            boneDialogue = int(input('1: Do the Bull Charge (Mike Tysons Punch Out), 2: Eat it, 3: Ask for forbidden knowledge, 4: Fight'))
        if boneDialogue == 1:
            print('You Bull Charge your nemesis to Hell and back and earn NOTHING! You LOSE! GOOD DAY SIR!')
            return
        elif boneDialogue == 2:
            print('You choke on the bone and die in five minutes.')
        elif boneDialogue == 3:
            print('Where does he get his supply of laurels?') # In Castlevania II, some dude in Laruba Mansion gives you free laurels if you talk with him. He never exhausts his supply. Where does he get it?
            print('Before the bone responds, you are smitten by the ghost of Asa Griggs Candler. Game Over')
            

    def LichDialogue():
        print("LICH: Shall I pick your nose, good sir?")
        noseChoice = 5
        while noseChoice > 4 or noseChoice < 1:
            noseChoice = int(input("1: Let him pick your nose, 2: Don't let him pick your nose, 3: Blast him with your Colazooka, 4: Listen to a joke"))
        if noseChoice == 1:
            print('The lich shoves a Colazooka up your nose and pulls the trigger. You are now a pile of Mentos. Game Over')
        elif noseChoice == 2:
            print('Nothing happens. You fight anyway.')
        elif noseChoice == 3:
            print('The lich snatches it from you before you can use it. He pulls the trigger and you explode. GAME OVER')
        elif noseChoice == 4:
            print("LICH: where did the 7 go?")
            trashjokeChoice = 2
            while trashjokeChoice != 1:
                trashjokeChoice = int(input("1: "))
            if trashjokeChoice == 1:
                print("LICH: HOME! haha get it? he went HOME! get it cuz it says home on the 7 key? on the number pad!!!")
                print("The pain hurts worse than a spike up your pike.")
                jokeReaction = 2
                while jokeReaction != 1:
                    jokeReaction = int(input("1: just kill me at this point"))
                if jokeReaction == 1:
                    print("LICH: how dare you not laugh! lets fight!!!") # Look up 101 Wacky Computer Jokes for more info. I am not responsible for any cancers you get.

    def WizardDialogue():
        print("WIZARD: uhuhuhuh... kids shows funny... uhhuhuhh...")
        wizardChoice = 5
        while wizardChoice > 4 or wizardChoice < 1:
            wizardChoice = int(input("1: Kick 'it' to him, 2: Ask for his age, 3: Pick your nose, 4: Ask for his weight"))
        if wizardChoice == 1:
            print('WIZARD picks his nose all the time. FIGHT!')
        elif wizardChoice == 2:
            print("me 31 years old lel") # prime number
        elif wizardChoice == 3:
            print("Before you can eat it, the wizard slaps your boogers out of your hand and challenges you to a duel. FIGHT!")
        elif wizardChoice == 4:
            print("The wizard tips over and crushes you with his immense weight. Oops.")

    def wormDialogue(): # pop musicians deserve to have colazookas shoved up their hinies until they submit to the coca cola company
        print("WORM: jfjiefjiwejwfjiweef")
        wormChoice = 4
        while wormChoice > 3 or wormChoice < 1:
            wormChoice = int(input("1: 'The government is controlled by PepsiCo', 2: 'Christmas is in May,' 3: phhhhtphtphtphtphtphp"))
        if wormChoice == 1:
            print('WORM: FAKE! lets fight')
        elif wormChoice == 2: # to infinity and beyond
            print('WORM: You got that right. LETS FIGHT ANYWAY!')
        elif wormChoice == 3:
            print('You spat on the worm. FIGHT!!')

    def medusaDialogue():
        print("MEDUSA: oh baby baby baby OOOOOHHH oh baby baby baby NOOOOOOOO")    
        medusaChoice = 4
        while medusaChoice > 3 or medusaChoice < 1:
            medusaChoice = int(input("1: Stay and listen, 2: Fling boogers at her, 3: Sing an equally bad song"))
        if medusaChoice == 1:
            print("You turn to stone and die. FIGHT ANYWAY!")
        elif medusaChoice == 2:
            print("She stops and flings them back in your mouth. FIGHT!")
        elif medusaChoice == 3:
            print("Rebecca Black deserves a Colazooka up the hiney. FIGHT!")

    def karyDialogue():
        print("KARY: I have been picking my nose for the past five hours")
        karyChoice = 5
        while karyChoice > 4 or karyChoice < 1:
            karyChoice = int(input("1: Pick its nose, 2: Punch it in the face, 3: Start a conspiracy theory, 4: Sing that one song from Histeria"))
        if karyChoice == 1:
            print("Your fingers explode and become cans of Coke. GAME OVER")
        elif karyChoice == 2:
            print("OGRE FIGHT!!")
        elif karyChoice == 3: 
            print("Santa Claus is a hoax created by the government to get kids to punch people in the face.")
        elif karyChoice == 4:
            print("creating terror and government purges acting out all of your monstrous urges big brother plots that would make orwell blush these are the things that sure give me a rush spying on lenin and murdering trotsky vexing the west with his communist plotsky turning your dreams into scary nightmares that is the way i forget all my cares when the germans invade moscow and the weather's vile i simply look on as they all freeze to death and that really makes me smile feasting like ivan while serfs live in rations conquering dozens of satellite nations starting my own personality cult doing away with those who might revolt sending your critics to rot in siberia thats how you get populations to fear ya building a wall down the streets of berlin this kind of thing makes me flash quite a grin if the people call for freedom or democracy i simply bump off everybody until theres nobody left but me")

    def krakenDialogue():
        print("KRAKEN: i am dead") # do not try this at home
        krakenChoice = 4
        while krakenChoice > 3 or krakenChoice < 1:
            krakenChoice = int(input("1: No you're not, 2: you are right, 3: i punched a tv in the face and got a heart attack"))
        if krakenChoice == 1:
            print("KRAKEN: PROVE IT")
            existChoice = 2
            while existChoice != 1:
                existChoice = int(input("1: the dead cannot speak"))
            if existChoice == 1:
                print("KRAKEN: ghosts speak and are dead, are you stupid?")
                ghostChoice = 4
                while ghostChoice > 3 or ghostChoice < 1:
                    ghostChoice = int(input("1: wow you're right, 2: ghosts are fake, 3: i punched a nanny in the face next five afternoons"))
                if ghostChoice == 1:
                    print("KRAKEN: about you? sure, why not")
                    suckChoice = 2
                    while suckChoice != 1:
                        suckChoice = int(input("Punch him in the face? 1: Yes"))
                    if suckChoice == 1:
                        print("FIGHT")
                elif ghostChoice == 2:
                    print("KRAKEN: uhhhh... zombies speak and they're dead. checkmate")
                    zombieChoice = 4
                    while zombieChoice > 3 or zombieChoice < 1:
                        zombieChoice = int(input("1: wow you're right, 2: they're undead. thats completely different, 3: i want pizza"))
                    if zombieChoice == 1:
                        print("KRAKEN: i win")
                        print("You explode because Kraken is right. GAME OVER")
                    elif zombieChoice == 2:
                        print("KRAKEN: but theyre real")
                        realChoice = 2
                        while realChoice != 1:
                            realChoice = int(input("1: no they aren't"))
                        if realChoice == 1:
                            print("KRAKEN: whatever I'm still dead")
                            deadChoice = 2
                            while deadChoice != 1:
                                deadChoice = int(input("1: how are you speaking then"))
                            if deadChoice == 1:
                                print("Kraken is mad. FIGHT!")
                    elif zombieChoice == 3:
                        print("KRAKEN: come and get some!!!")
                        print("FIGHT!!")
                elif ghostChoice == 3:
                    print("KRAKEN: what was that last part?")
                    nannyChoice = 2
                    while nannyChoice != 1:
                        nannyChoice = int(input("1: next five afternoons, why?"))
                    if nannyChoice == 1:
                        print("KRAKEN: are you on drugs???")
                        substanceChoice = 2
                        while substanceChoice != 1:
                            substanceChoice = int(input("1: caffeine, thank you very much"))
                        if substanceChoice == 1:
                            print("KRAKEN: you like coffee?")
                            coffeeChoice = 3
                            while coffeeChoice > 2 or coffeeChoice < 1:
                                coffeeChoice = int(input("1: yes, 2: no"))
                            if coffeeChoice == 1:
                                print("KRAKEN: huh me too... lets fight")
                            elif coffeeChoice == 2:
                                print("KRAKEN: bad for you... lets fight")
        elif krakenChoice == 2:
            print("KRAKEN: ya like jazz")
            BeeMovieChoice = 2
            while BeeMovieChoice != 1:
                BeeMovieChoice = int(input("1: yes"))
            if BeeMovieChoice == 1:
                print("bee movie") # placeholder for the entire script
                print("FIGHT")
        elif krakenChoice == 3:
            print("KRAKEN: when are ya getting married?")
            marriageChoice = 3
            while marriageChoice > 2 or marriageChoice < 1:
                marriageChoice = int(input("1: to whom? 2: NEVER!!!"))
            if marriageChoice == 1:
                print("KRAKEN: the tv, genius")
                tvChoice = 3
                while tvChoice > 2 or tvChoice < 1:
                    tvChoice = int(input("1: no I'm a phone man!!! 2: of course"))
                if tvChoice == 1:
                    print("KRAKEN: thats stupid. lets fight")
                elif tvChoice == 2:
                    print("KRAKEN: alright. lets dance")
            elif marriageChoice == 2:
                print("KRAKEN: bad for you. lets fight")

    def tiamatDialogue():
        print("TIAMAT: what is love?")
        loveChoice = 4
        while loveChoice > 3 or loveChoice < 1:
            loveChoice = int(input("1: baby don't hurt me, 2: i'm not your english teacher. look it up, 3: leave"))
        if loveChoice == 1:
            print("TIAMAT: no more...")
            nomoreChoice = 4
            while nomoreChoice > 3 or nomoreChoice < 1:
                nomoreChoice = int(input("1: What is love? 2: Pulverize him, 3: Stop speaking"))
            if nomoreChoice == 1:
                print("TIAMAT: you ain't never gettin' it")
                print("FIGHT!")
            elif nomoreChoice == 2:
                print("you asked for it. FIGHT!!")
            elif nomoreChoice == 3:
                print("...")
                print("TIAMAT: speak")
                speakChoice = 3
                while speakChoice > 2 or speakChoice < 1:
                    speakChoice = int(input("1: Don't speak, 2: Pick your nose"))
                if speakChoice == 1:
                    print("TIAMAT: lets fight. call uncle")
                elif speakChoice == 2:
                    print("TIAMAT: EW what the hell?!!?! use a tissue!!!!11111!!1!one!1111!")
                    snotChoice = 4
                    while snotChoice > 3 or snotChoice < 1:
                        snotChoice = int(input("1: Eat it, 2: Wipe it on TIAMAT, 3: Wipe it on your underwear"))
                    if snotChoice == 1:
                        print("TIAMAT: THATS DISGUSTING WTF?! YOU SHALL DIE!!!!!!!!!!!!!!!!!!!!!1111111111111one")
                    elif snotChoice == 2:
                        print("TIAMAT: STOP WHAT THE HELL?! GROSS IT HURTS LIKE HELL RUN AWAY RUN AWAYYYYYY")
                    elif snotChoice == 3:
                        print("TIAMAT: EWWW WHAT THE HELL THATS DISGUSTING!!! DONT EVER DO THAT AGAIN!!! EVER!!!!!!")
                    print("FIGHT!!")
        if loveChoice == 2:
            print("TIAMAT: shut up")
            shutupChoice = 2
            while shutupChoice != 1:
                shutupChoice = int(input("1: takes one to know one"))
            if shutupChoice == 1:
                print("TIAMAT: speak for yourself mr. or mrs. brain damage.")
        if loveChoice >= 3:
            print("TIAMAT: alright")

    def chaosDialogue():
        print("CHAOS: oh dear lord... what are you doing in my house? are you Barry B Benson?")
        barryChoice = int(input("1: Yes"))
        if barryChoice == 1:
            beelaw1 = "get the answer"
            while beelaw1 != "absolutely no talking to humans":
                beelaw1 = str(input('CHAOS: whats bee law number 1? all lowercase'))
                beelaw1.lower()
            if beelaw1 == "absolutely no talking to humans":
                print("CHAOS: man you're good. now gimme my package")
                packageChoice = "get the answer"
                while packageChoice != 1:
                    packageChoice = int(input("1: what package?"))
                if packageChoice == 1:
                    print("CHAOS: the honey, idiot. you've gotta start thinking bee. i dont feed my kids for nothing") # THINKING BEE! THINKING BEE! THINKING BEE!
                    honeyChoice = 2
                    while honeyChoice != 1:
                        honeyChoice = int(input("1: I lost it"))
                    if honeyChoice == 1:
                        print("CHAOS: how did you lose it?")
                        lossChoice = 2
                        while lossChoice != 1:
                            lossChoice = int(input("1: uhhhh..."))
                        if lossChoice == 1:
                            print("CHAOS: you're not Barry B. Benson. are you a florist?")
                            florismChoice = 3
                            while florismChoice > 2 or florismChoice < 1:
                                florismChoice = int(input("1: yes"))
                            if florismChoice == 1:
                                florist = str(input("CHAOS: alright tell me your name."))
                                if florist == "Vanessa Bloome":
                                    print("CHAOS: oh goody! show me your roses")
                                    roseChoice = 2
                                    while roseChoice != 1:
                                        roseChoice = int(input("1: what roses?"))
                                    if roseChoice == 1:
                                        print("CHAOS: forget that last part, are you her husband?")
                                        husbandChoice = 3
                                        while husbandChoice > 2 or husbandChoice < 1:
                                            husbandChoice = int(input("1: Yes, 2: No"))
                                        if husbandChoice == 1:
                                            allergy = str(input("CHAOS: allergies?"))
                                            if allergy == "bees":
                                                print("CHAOS: what do you think of bees?")
                                                beeChoice = 2
                                                while beeChoice != 1:
                                                    beeChoice = int(input("1: I don't know"))
                                                if beeChoice == 1:
                                                    print("CHAOS: you're a liar. hold on to your honey bucko")
                                            else:
                                                print("CHAOS: in five minutes that will be you. let's fight")
                                        elif husbandChoice == 2:
                                            print("CHAOS: thank you for your honesty. die anyway")
                                else:
                                    print("CHAOS: you're a liar. get me a pizza")
                                    pizzaChoice = 2
                                    while pizzaChoice != 1:
                                        pizzaChoice = int(input("1: why?"))
                                    if pizzaChoice == 1:
                                        print("CHAOS: my kids would love that")
                                        kidsChoice = 2
                                        while kidsChoice != 1:
                                            kidsChoice = int(input("1: i got nothing"))
                                        if kidsChoice == 1:
                                            print("CHAOS: there was literally a pizza man whom you beat the crap out of")
                                            pizzamanChoice = 1
                                            while pizzamanChoice != 1:
                                                pizzamanChoice = int(input("1: that was an imp what do you mean?"))
                                            if pizzamanChoice == 1:
                                                print("CHAOS: imp? what do you mean 'imp?!' he's critically wounded and is in the hospital!")
                                                woundsChoice = 2
                                                while woundsChoice != 1:
                                                    woundsChoice = int(input("1: ok and?"))
                                                if woundsChoice == 1:
                                                    print("CHAOS: HE WAS 14! what the hell did he do to you?!")
                                                    fourteenChoice = 2
                                                    while fourteenChoice != 1:
                                                        fourteenChoice = int(input("1: he hit me in the face with a pizza box"))
                                                    if fourteenChoice == 1:
                                                        print("CHAOS: ...because you KICKED HIM OFF HIS BIKE AND ONTO THE PAVEMENT! have you been living under a rock?! and what about that man with cotard's syndrome?!") # it's a condition where someone thinks they're dead or have missing body parts, organs, blood, etc.
                                                        syndromeChoice = 2
                                                        while syndromeChoice != 1:
                                                            syndromeChoice = int(input("1: you mean the kraken?"))
                                                        if syndromeChoice == 1:
                                                            print("CHAOS: HE HAD THREE KIDS AND TWO NEPHEWS! NOW HE'S DEAD. I READ IT IN THE NEWS. GOOD JOB. YOU'RE SO HELPFUL. *beep boop beep*")
                                                            print("DISPATCHER: 911 what's your emergency?")
                                                            print("CHAOS: theres an escaped mental patient in my house! 19321 rock avenue! come quickly!!! *hang up* while they arrive i'll have my wife and kids fight you!")
                                                            # kary.fight()
                                                            # kraken.fight()
                                                            # tiamat.fight() # why do we have to fight him again if he's optional
                                                            print("CHAOS: YOU DARE KILL MY WIFE AND CHILDREN??? I WILL KILL YOU AND KICK YOU IN THE HINEY!") #
                                                            print("1: i don't care")
                                                            print("CHAOS: you wanna do it the hard way? i'll feed you oatmeal raisin cookies for eternity!")
                                                            print("1: n-no don't do this to me")
                                                            print("CHAOS: WHILE YOU'RE AT IT I'LL MAKE YOU LISTEN TO JUSTIN BIEBER...")
                                                            print("1: NO! NO! DONT HURT ME!! HELP!!!")
                                                            print("CHAOS: and ill make you watch cooking shows set to chargeman ken! hahahahahahahhahahah") # pure evil!!!!!
                                                            print("1: NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
                                                            print("CHAOS: that is if i win")
                                                            print('1: alright bring it on!')
    chaosDialogue()

# def swap():
#     x = float(input("type a number"))
#     y = float(input("type another number"))
#     if x > y:
#         x = (y - x)
#         y = (y - x)
#         x = (x + y)
#     elif x < y:
#         y = (x - y)
#         x = (x - y)
#         y = (x + y)
#     print(x)
#     print(y)
# swap()