name = input("Hello Adventurer! What is your name? ")
hp = 100 
hp_t = 100
exp = 0 
gold = 100
hit = 0.7
power = 30
item = "Wooden Sword"
armor = "none"

def change_hp(hp,HP,hp_t):
    output(hp)
    if HP + hp > hp_t:
        HP = (HP + hp) - hp_t
        output("You have reached your maximum hp! ")
    hp += HP
    if HP > 0:
        output(f"Your hp was increased by {abs(HP)} ")
    if HP < 0:
        output(f"Your hp was decreased by {abs(HP)} ")
    output(f"Your current hp is {hp}")

def change_exp(exp, EXP):
    exp += EXP
    if EXP >= 0:
        output(f"Your exp increased by {abs(EXP)}")
    output(f"Your new exp is {exp} ")

def change_gold(gold, GOLD):
    if gold - GOLD < 0:
        output("You do not have enough gold for this item")
    else:
        gold += GOLD
        if GOLD > 0:
            output(f"You gained {abs(GOLD)} gold")
        if GOLD < 0:
            output(f"You lost {abs(GOLD)} gold")
    output(f"You have {gold} gold left")





