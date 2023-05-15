from classes import *
from attack import *
from actions import *




def attack(self):
    random_p = int(power * (random.randint(80, 120)/100))
    output(f"The {self.name} takes {random_p} damage")
    self.hp -= random_p
    if self.hp < 0:
        self.hp = 0
    output(f"The {self.name}'s new hp is {self.hp}")



def fight(self):
   while hp > 0 and self.hp > 0:
        output(f"Your HP: {hp}")
        output(f"{self.name}'s HP: {self.hp}")
        move = False
        while move == False:
            choice = int(input("1. Attack 2. Magic"))
            if choice == 1:
                output(f"You attack the {self.name}")
                self.attacked()
                move = True
            if choice == 2:
                if magic_num < 1:
                    output("You havent learned any magic yet")
                else:
                    if magic_num > 0:
                        print("1. Fire",end=" ")
                    if magic_num > 1:
                        print("2. Dark",end=" ")
                    if magic_num > 2:
                        print("3. Heal",end=" ")     
                    if magic_num > 3:
                        print("4. Stun",end=" ")     
                    if magic_num > 4:
                        print("5. DOOM",end="")    
                    magic_choice = int(input(("What magic would you like to use?")))
                if magic_choice <= magic_num and magic_choice > 0:
                    if magic_choice == 3:
                        heal = (20 + random.randint(1,10))
                        hp += heal
                        if hp > hp_t:
                            hp = hp_t
                        output(f"You gained {heal} hp")
                    else: 
                        self.magic(magic_num)
                                                                                             
        if(self.hp > 0 and self.check_stun() == False):
            output(f"The {self.name}{self.weapon}")
            self.attack(hp)

troll.fight()
