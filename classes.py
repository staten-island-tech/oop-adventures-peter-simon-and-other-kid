import random
import sys
import time

magic = {}
def test(prob):
    return random.randint(0,1) > prob


class Output:
    def __init__(self,typing_speed):
        self.typing_speed = typing_speed
    def output(self,t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random()*10.0/self.typing_speed)
        print('')

   




class User:
    user_output = Output(130)
    def __init__(self):
        self.name = ""
        self.hp = 100

        self.hp_t = 100
        self.exp = 0 
        self.gold = 100
        self.hit = 0.7
        self.power = 30
        self.item = "Wooden Sword"
        self.armor = "none"
        self.magic_num = 0

    def change_hp(HP):
        user_output.output(hp)
        if HP + hp > hp_t:
            HP = (HP + hp) - hp_t
            user_output.output("You have reached your maximum hp! ")
        hp += HP
        if HP > 0:
            user_output.output(f"Your hp was increased by {abs(HP)} ")
        if HP < 0:
            user_output.output(f"Your hp was decreased by {abs(HP)} ")
        user_output.output(f"Your current hp is {hp}")

    def change_exp(EXP):
        exp += EXP
        if EXP >= 0:
            user_output.output(f"Your exp increased by {abs(EXP)}")
        user_output.output(f"Your new exp is {exp} ")

    def change_gold(GOLD):
        if gold - GOLD < 0:
            user_output.output("You do not have enough gold for this item")
        else:
            gold += GOLD
            if GOLD > 0:
                user_output.output(f"You gained {abs(GOLD)} gold")
            if GOLD < 0:
                user_output.output(f"You lost {abs(GOLD)} gold")
        user_output.output(f"You have {gold} gold left")
    def die(self):
        print("Game Over!")
        exit()

class weapon:
    def __init__(self,power,hit,name):
        self.power = power
        self.hit = hit
        self.name = name
    
    def equip(self):
        print(f"{self.name} equiped")
        hit = self.hit
        power = self.power
        weapon = self.name
    
    
class monster:
    fight_attacked_output = Output(200)
    def __init__(self,hp,power,hit,level,name,weapon):
        self.hp = hp
        self.power = power
        self.hit = hit
        self.name = name
        self.level = level
        self.stun = False
        self.weapon = weapon
    def attacked(self):
        random_p = int(power * (random.randint(80, 120)/100))
        fight_attacked_output.output(f"The {self.name} takes {random_p} damage")
        self.hp -= random_p
        if self.hp < 0:
            self.hp = 0
        fight_attacked_output.output(f"The {self.name}'s new hp is {self.hp}")

    def attack(self):
        global hp
        random_p = int(self.power * (random.randint(80, 120)/100))
        if random.random() < self.hit:
            fight_attacked_output.output(f"You take {random_p} damage")
            hp -= random_p
            if hp < 0:
                die()
        else:
            print(f"The {self.name} missed!")
    
    def fight(self):
        global hp
        global magic_num
        while hp > 0 and self.hp > 0:
            fight_attacked_output.output(f"Your HP: {hp}")
            fight_attacked_output.output(f"{self.name}'s HP: {self.hp}")
            move = False
            while move == False:
                choice = int(input("1. Attack 2. Magic"))
                if choice == 1:
                    fight_attacked_output.output(f"You attack the {self.name}")
                    self.attacked()
                    move = True
                if choice == 2:
                    if magic_num < 1:
                        fight_attacked_output.output("You havent learned any magic yet")
                    else:
                        if magic_num > 0:
                            print("1.Fire",end=" ")
                        if magic_num > 1:
                            print("2.Dark",end=" ")
                        if magic_num > 2:
                            print("3.Heal",end=" ")     
                        if magic_num > 3:
                            print("4.Stun",end=" ")     
                        if magic_num > 4:
                            print("5.DOOM",end="")    
                        print()
                        magic_choice = int(input(("What magic would you like to use?")))
                        if magic_choice <= magic_num and magic_choice > 0:
                            move = True
                            if magic_choice == 3:
                                heal = (20 + random.randint(1,10))
                                hp += heal
                                if hp > hp_t:
                                    hp = hp_t
                                fight_attacked_output.output(f"You gained {heal} hp")
                                fight_attacked_output.output(f"Your new hp is {hp}")
                            else: 
                                self.magic(magic_choice)
                        else: 
                            print("Please enter a valid magic number")
            if(self.hp > 0):
                if(self.check_stun() == False):

                    fight_attacked_output.output(f"The {self.name} {self.weapon}")
                    self.attack()
                else:
                    print(f"The {self.name} is stunned!")
    def magic(self,num):
        if num == 1:
            random_p =20 + random.randint(1,10)
            self.hp -= random_p
            fight_attacked_output.output(f"The {self.name} takes {random_p} damage")
        if num == 2:
            self.hit -= 0.3
            fight_attacked_output.output("Darkness applied")
        if num == 4:
            if self.level < 5:
                self.stun = True
            else:
                fight_attacked_output.output("Stun is ineffective")
        if num == 5:
            random_p = 100 + random.randint(1,100)
            self.hp -= random_p
            fight_attacked_output.output(f"The {self.name} takes {random_p} damage")

    def check_stun(self):
        if self.stun == True:
            if(self.level > 4):
                fight_attacked_output.output(f"{self.name} is cured from stun!")
                self.stun = False
                self.level = 6
                return False
            else:
                self.level += 1
                return True
        else:
            return False


class boss(monster):
    def __init__(self,hp,power,hit,level,name,weapon):
        super().__init__(hp,power,hit,level,name, weapon)

""" 
    def nuke(self):
        nuke_damage = 50 + random.randint(0, 10)
        if test(self.magic):
            change_hp(nuke_damage)
        else:
            fight_attacked_output("Nuke was ineffective")
 """
class armor:
    def __init__(self,bonus,name):
        self.bonus = bonus
    
    def equip(self):
        hp = 100 + self.bonus
        armor = self.name
        

# Declare monsters
bartender = monster(50,10,0.5,1,"Bartender","blasts you with his colazuka")
troll = monster(50,15,0.7,1,"Troll","pulls out his pizza box and whacks you")
wolf = monster(80,25,0.6,2,"Wolf", "lunges and bites you")
bone = monster(120,30,0.8,2,"Bone", "punches you")
lich = monster(150,50,0.8,3,"Lich", "yells bad jokes at you until your brain starts hurting")
wizard = monster(150,44,0.9,3,"Wizard", "blasts a fireball at you")
worm = monster(200,30,0.9,3,"Worm", "trips over a cheerio and launches it at you")
medusa = monster(200,35,0.9,3,"Medusa", "gazes into your soul")
kary = monster(300,50,0.85,4,"Kary", "covers you in oil and lights you on fire")
kraken = monster(400,60,0.8,4,"Kraken", "squeezes you with his tenticle")
tiamat = monster(420,40,0.95,4,"Tiamat", "spawns as lightning cloud above you and it shoots lightning on your head")
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

