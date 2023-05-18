from classes import *
from actions import *

def intro():
    output("Once Upon a Time....")
    time.sleep(1)
    output("Long ago, peace was restored. Monsters were eliminated")
    output("The five main evil forces were locked up, Lich, Kary, Kraken, Tiamat, and their boss, Chaos")
    output("They once covered the war in darkness until, the light warrior beat them all")
    output("You forgot who you were after they escaped and wiped your memory")
    output(f"You are {name}, the famous light warrior that destroyed these evil forces")
    output("Upon the escape of the evils, they released numerous monsters to guard their castle")
    output("Go! defeat the five evils and restore the world once again!")
    output("I am only a spirit and can only do so much, so I have left my friend to help you")
    output("He is a mushroom that will guide you to the monsters")
    output("Here, take this wooden sword, you will need it")
    wooden.equip()



intro()