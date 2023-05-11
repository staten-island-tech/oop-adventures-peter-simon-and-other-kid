import random
from actions import *


magic = {}
def test(prob):
    return random.randint(0,1) > prob


typing_speed = 70 #wpm
def output(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

class weapon:
    def __init__(self,power,hit,name):
        self.power = power
        self.hit = hit
        self.name = name
    
    def equip(self):
        hit = self.hit
        power = self.power
        weapon = self.name
    
    
class monster:
    def __init__(self,hp,power,hit,level,name,weapon):
        self.hp = hp
        self.power = power
        self.hit = hit
        self.name = name
        self.level = level
        self.stun = False
    def attacked(self):
        random_p = int(power * (random.randint(80, 120)/100))
        output(f"The {self.name} takes {random_p} damage")
        self.hp -= random_p
        if self.hp < 0:
            self.hp = 0
        output(f"The {self.name}'s new hp is {self.hp}")

    def attack(self):
        random_p = int(power * (random.randint(80, 120)/100))
        output(f"The {self.name} takes {random_p} damage")
        self.hp -= random_p
        if self.hp < 0:
            self.hp = 0
        output(f"The {self.name}'s new hp is {self.hp}")

    def magic(self,num):
        if num == 1:
            random_p = self.hp - (20 + random.randint(1,10))
            self.hp -= random_p
            output(f"The {self.name} takes {random_p} damage")
        if num == 2:
            self.hit -= 0.3
            output("Darkness applied")
        if num == 4:
            if self.level < 5:
                self.stun == True
                output(f"{self.name} is stunned")
            else:
                output("Stun is ineffective")
    
    def check_stun(self):
        if self.stun == True:
            if(self.level > 4):
                output(f"{self.name} is cured from stun!")
                return False
            else:
                self.level += 1
                return True


class boss(monster):
    def __init__(self,hp,power,hit,level,name,weapon):
        super().__init__(hp,power,hit,level,name, weapon)

""" 
    def nuke(self):
        nuke_damage = 50 + random.randint(0, 10)
        if test(self.magic):
            change_hp(nuke_damage)
        else:
            output("Nuke was ineffective")
 """
class armor:
    def __init__(self,bonus,name):
        self.bonus = bonus
    
    def equip(self):
        hp = 100 + self.bonus
        armor = self.name
        

# Declare monsters
bartender = monster(50,10,0.5,1,"Bartender","blasts you with his colazuka")
troll = monster(50,15,0.7,1,"troll","pulls out his pizza box and whacks you")
wolf = monster(80,25,0.6,2,"wolf", "lunges and bites you")
bone = monster(120,30,0.8,2,"bone", "punches you")
lich = monster(150,50,0.8,3,"lich", "yells bad jokes at you until your brain starts hurting")
wizard = monster(150,44,0.9,3,"wizard", "blasts a fireball at you")
worm = monster(200,30,0.9,3,"worm", "trips over a cheerio and launches it at you")
medusa = monster(200,35,0.9,3,"medusa", "gazes into your soul")
kary = monster(300,50,0.85,4,"kary", "covers you in oil and lights you on fire")
kraken = monster(400,60,0.8,4,"kraken", "squeezes you with his tenticle")
tiamat = monster(420,40,0.95,4,"tiamat", "spawns as lightning cloud above you and it shoots lightning on your head")
chaos = boss(600,80,0.9,5,"CHAOS","throws a nuke at you")

# Declare weapons
wooden = weapon(30,0.7,"Wooden Sword")
iron = weapon(50,0.8,"Iron Sword")
silver = weapon(55,0.82,"Silver Mace")
titanium = weapon(75,0.92,"Titanium Halberd")
gold = weapon(80,0.95,"Golden Scimitar")
diamond = weapon(100,0.98,"Diamond Greatsword")

#Declare armor
leather = armor(10, "Leather Armor")
iron = armor(20, "Iron Armor")
silver = armor(40,"Silver Armor")
titanium = armor(75, "Titanium Armor")
gold = armor(100, "Gold Armor")
diamond = armor(150, "Diamond") 