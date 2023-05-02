name = input("Hello Adventurer! What is your name? ")
hp = 100 
hp_t = 100
exp = 0 
gold = 100


def change_hp(hp,HP,hp_t):
    print(hp)
    if HP + hp > hp_t:
        HP = (HP + hp) - hp_t
        print("You have reached your maximum hp! ")
    hp += HP
    if HP > 0:
        print(f"Your hp was increased by {abs(HP)} ")
    if HP < 0:
        print(f"Your hp was decreased by {abs(HP)} ")
    print(f"Your current hp is {hp}")

def change_exp(exp, EXP):
    exp += EXP
    if EXP >= 0:
        print(f"Your exp increased by {abs(EXP)}")
    print(f"Your new exp is {exp} ")

def change_gold(gold, GOLD):
    if gold - GOLD < 0:
        print("You do not have enough gold for this item")
    else:
        gold += GOLD
        if GOLD > 0:
            print(f"You gained {abs(GOLD)} gold")
        if GOLD < 0:
            print(f"You lost {abs(GOLD)} gold")
    print(f"You have {gold} gold left")





