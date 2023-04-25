

class weapon:
    def __init__(self,power,hit,name):
        self.power = power
        self.hit = hit
        self.name = name
    
class armor:
    def __init__(self,absorb,name):
        self.absorb = absorb
        self.name = name
    
class location:
    def __init__(self,monster):
        self.monster = monster

class monster:
    def __init__(self,hp,power,hit,absorb,level,name):
        self.hp = hp
        self.power = power
        self.hit = hit
        self.absorb = absorb
        self.name = name
    
    def attack(self)
    


# Declare monsters
imp = monster(50,10,0.5,0,1,"imp")
troll = monster(50,15,0.7,1,1,"troll")
wolf = monster(80,25,0.6,1,2,"wolf")
bone = monster(120,30,0.8,3,2,"bone")
lich = monster(150,50,0.8,5,3,"lich")
wizard = monster(150,44,0.9,5,3,"wizard")
worm = monster(200,30,0.9,5,3,"worm")
medusa = monster(200,35,0.9,3,3,"medusa")
kary = monster(300,50,0.85,7,4,"kary")
kraken = monster(400,60,0.8,8,4,"kraken")
tiamat = monster(420,40,0.95,10,4,"tiamat")
chaos = monster(600,80,0.9,12,5,"CHAOS")

# Declare weapons
wooden = weapon(30,0.7,"Wooden Sword",1)
iron = weapon(50,0.8,"Iron Sword",2)
silver = weapon(55,0.82,"Silver Mace",3)
titanium = weapon(75,0.92,"Titanium Halberd",4)
gold = weapon(80,0.95,"Golden Scimitar",5)
diamond = weapon(100,0.98,"Diamond Greatsword",6)

def options():
    print("1. Search Around")
    print("")
    print("")



while won != true:
    print("You are in a dark room")

    input("")