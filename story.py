import time
from classes import Output
from classes import wooden
story = Output()
def intro(name):
    time.sleep(1)
    story.output("Long ago, peace was restored. Monsters were eliminated")
    time.sleep(1)
    story.output("The five main evil forces were locked up, Lich, Kary, Kraken, Tiamat, and their boss, Chaos")
    time.sleep(1)
    story.output("They once covered the war in darkness until, the light warrior beat them all")
    time.sleep(1)
    story.output("You forgot who you were after they escaped and wiped your memory")
    time.sleep(1)
    story.output(f"You are {name}, the famous light warrior that destroyed these evil forces")
    time.sleep(1)
    story.output("Upon the escape of the evils, they released numerous monsters to guard their castle")
    time.sleep(1)
    story.output("Go! defeat the five evils and restore the world once again!")
    time.sleep(1)
    story.output("I am only a spirit and can only do so much, so I have left my friend to help you")
    time.sleep(1)
    story.output("He is a mushroom that will guide you away from monsters")
    time.sleep(1)
    story.output("Here, take this wooden sword, you will need it")
    wooden.equip()
    time.sleep(1)
    story.output("I have to go now, but save the world!")
    time.sleep(2)
    story.output("TOAD: Hey Im Toad, I'm going to help you on your journey")
    time.sleep(1)
    story.output("TOAD: I don't know about you, but I'm Staaaaaarrrrrvviiiinnnnnngnggggg!")
    time.sleep(1)
    story.output(f"{name.upper()}: Same!, lets get something to eat")
    time.sleep(1)
    story.output("TOAD: I know a good place to get a drink around here. Follow me!")

def forest(name):
    global magic_num
    story.output("TOAD: Lets try to stay clear from any monsters when we hike through this forest")
    story.output("TOAD: Oh! and by the way, let me teach you some magic before we continue")
    story.output("TOAD: Brace yourself!, I'm going to transfer a spell into you")
    story.output("TOAD: I am have to shout a random bee movie script line for it to work")
    story.output("TOAD:Ready?")
    
    time.sleep(1)
    for i in range(100):
        print("You're flying outside the hive, talking to humans that attack our homes with the power washers and M-80s! One eighth a stick of dynamite!")
        time.sleep(0.04)
    magic_num += 1
    story.output("TOAD: Alright!, I just transfered a fire spell into you. You can now use it in battle!")
    story.output(f"{name.upper()}: I feel a little uneasy")
    story.output("TOAD: That's normal for your first spell, don't worry, you will get used to it")
    story.output("TOAD: Now, Onward!")
    story.output("TOAD: We are almost near the reed forests, be careful for monsters")
    story.output("TOAD: Look, an imp ahead!, be careful, these creatures can be very dangerous")

def reed(name):
    story.output("TOAD: That was a close one! lets continue on, there should be only two more miles until we get to the Lich")
    story.output("TOAD: 1 mile in.....")
    story.output("TOAD: Pheeeeeooo, Im tired, lets call it a day for today")
    story.output("TOAD: Alright, I'm going to sleep, you keep guard. Be careful, there are many trolls here. Here, take my Golden Scimitar")
    gold.equip()
    story.output("TOAD: zzzzzzzzzzzzzzzzzzzz")
    story.output(f"{name.upper()}: Gosh, I'm tired, I dont know how long I can stay awake for *Yawn*")
    story.output(f"{name.upper()}: It wont hurt if I go to sleep, I dont see any trolls anyway")
    story.output(f"{name.upper()}: zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    story.output("*Morning time*")
    story.output("TOAD: W-where are we?")
    story.output(f"{name.upper()}: I think we are in a trolls lair")
    story.output("TOAD: LET US OUT OF HEERRRRREEE!!!!!!!!!!")

def bone_story():
    story.output("TOAD: Look a bone!")
    story.output("TOAD: Beware, the bone might look weak but his attacks pack a punch!")
    story.output("You stare at the Bone")
    story.output("...")
    Story.output("TOAD: Go on now, I'll watch")

def lich_story():
    story.output("The room falls into darkness, a LICH appears")
    story.output("TOAD: The lich is the first of CHAOS' bosses. He can be very dangerous")
    story.output("TOAD: Try and attack his weak spot...")
    story.output("...")
    story.output("TOAD: WELL I'M NOT GONNA TELL YOU WHAT IT IS")

def wizard_story():
    story.output("TOAD: Behold the keeper of Magic, the almighty Wizard")

def worm_story():
    story.output("WIZARD: Alright, ill give you my magic")
    for i in range(100):
        print("Dddddddddaaaaaaaaaaaaaaaarrrrrrrrrrrrrrkkkkkkkkkkkkkkkknnnnnnnnnnnneeeeeeeeeeeeessssssssssssssssss sppppppeeeeeeeeeeeeeeeellllllllllllllllllllll")
        time.sleep(0.04)
    magic_num += 1
    story.output("WIZARD: Alright, you have learned a spell. Use it wisely. If you want to learn more, go and fight the worm. He has the mouth of horrible singing. Get that if you want to learn a spell")
    story.output("WIZARD: Now Leave!")
    story.output("TOAD: C'mon lets go!")
    story.output("*You arrive at the worms castle*")
    story.output("TOAD: *knock* *knock* *knock*")

