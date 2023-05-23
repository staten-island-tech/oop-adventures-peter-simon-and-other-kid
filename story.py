from classes import output

from actions import *
import time

def intro():
    output("olsidfgbh")
    time.sleep(1)
    output("Long ago, peace was restored. Monsters were eliminated")
    time.sleep(1)
    output("The five main evil forces were locked up, Lich, Kary, Kraken, Tiamat, and their boss, Chaos")
    time.sleep(1)
    output("They once covered the war in darkness until, the light warrior beat them all")
    time.sleep(1)
    output("You forgot who you were after they escaped and wiped your memory")
    time.sleep(1)
    output(f"You are {name}, the famous light warrior that destroyed these evil forces")
    time.sleep(1)
    output("Upon the escape of the evils, they released numerous monsters to guard their castle")
    time.sleep(1)
    output("Go! defeat the five evils and restore the world once again!")
    time.sleep(1)
    output("I am only a spirit and can only do so much, so I have left my friend to help you")
    time.sleep(1)
    output("He is a mushroom that will guide you away from monsters")
    time.sleep(1)
    output("Here, take this wooden sword, you will need it")
    wooden.equip()
    time.sleep(1)
    output("I have to go now, but save the world!")
    time.sleep(2)
    output("TOAD: Hey Im Toad, I'm going to help you on your journey")
    time.sleep(1)
    output("TOAD: I don't know about you, but I'm Staaaaaarrrrrvviiiinnnnnngnggggg!")
    time.sleep(1)
    output(f"{name.upper()}: Same!, lets get something to eat")
    time.sleep(1)
    output("TOAD: I know a good place to get a drink around here. Follow me!")

def forest():
    global magic_num
    output("TOAD: Lets try to stay clear from any monsters when we hike through this forest")
    output("TOAD: Oh! and by the way, let me teach you some magic before we continue")
    output("TOAD: Brace yourself!, I'm going to transfer a spell into you")
    output("TOAD: I am have to shout a random bee movie script line for it to work")
    output("TOAD:Ready?")
    
    time.sleep(1)
    for i in range(100):
        print("You're flying outside the hive, talking to humans that attack our homes with the power washers and M-80s! One eighth a stick of dynamite!")
        time.sleep(0.04)
    magic_num += 1
    output("TOAD: Alright!, I just transfered a fire spell into you. You can now use it in battle!")
    output(f"{name.upper()}: I feel a little uneasy")
    output("TOAD: That's normal for your first spell, don't worry, you will get used to it")
    output("TOAD: Now, Onward!")
    output("TOAD: We are almost near the reed forests, be careful for monsters")
    output("TOAD: Look, an imp ahead!, be careful, these creatures can be very dangerous")

def reed():
    output("TOAD: That was a close one! lets continue on, there should be only two more miles until we get to the Lich")
    output("TOAD: 1 mile in.....")
    output("TOAD: Pheeeeeooo, Im tired, lets call it a day for today")
    output("TOAD: Alright, I'm going to sleep, you keep guard. Be careful, there are many trolls here. Here, take my Golden Scimitar")
    gold.equip()
    output("TOAD: zzzzzzzzzzzzzzzzzzzz")
    output(f"{name.upper}: Gosh, I'm tired, I dont know how long I can stay awake for *Yawn*")
    output(f"{name.upper}: It wont hurt if I go to sleep, I dont see any trolls anyway")
    output(f"{name.upper}: zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    output("*Morning time*")
    output("TOAD: W-where are we?")
    output(f"{name.upper}: I think we are in a trolls lair")
    output("TOAD: LET US OUT OF HEERRRRREEE!!!!!!!!!!")

    