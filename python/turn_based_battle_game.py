import os
from random import random
from random import randint

class Player:
    def __init__(self, name, health, attacks, active):
        self.name = name
        self.health = health
        self.attacks = attacks
        self.active = active
        
win = False
        
user = Player("User", 100, {1:("Flurry of Blows", (18, 25)), 
                            2:("Hammerstrike", (10, 35)), 
                            3:("Rest", (18, 25))}, True)
                            
computer = Player("Comptuer", 100, {1:("light attack", (18, 25)), 
                                    2:("Moderate attack", (18, 35)), 
                                    3:("Heal", (18, 25))}, False)

command_message = "\nWhich attack would you like to use? >> [1-3] "

def print_attacks(attacker):
    print("\nCurrent health: {}".format(str(attacker.health)))
    print("Available attacks:\n")
    for attack in range(1,4):
        print(" " * 4 + str(attack) + "." + attacker.attacks[attack][0])
        
def do_combat(attack, attacker, defender):
    
    def end_turn(attacker, defender):
        global win
        
        if defender.health <= 0:
            print("\n##### Congratulations, {}!  You WIN!! #####".format(attacker.name))
            win = True
            
        attacker.active = False
        defender.active = True
    
    low = attacker.attacks[attack][1][0]
    high = attacker.attacks[attack][1][1]
    damage = randint(low, high)

    if attack != 3:
        defender.health -= damage 
        print("\n{} attacks {} with a {} for {} damage".format(attacker.name, defender.name, 
                                                             attacker.attacks[attack][0], 
                                                             damage))
        if defender.health <= 10:
            print("They're fading in and out!")
        elif defender.health <= 50:
            print("They can barely stand!")
    else:
        attacker.health += damage
        print("\n{} heals themself with {} for {} health".format(attacker.name, attacker.attacks[attack][0],
                                                               damage))
    
    print("\n{} health: {}".format(attacker.name, attacker.health))
    if defender.health >= 0:
        print("{} health: {}".format(defender.name, defender.health))
    else:
        print("{} health: 0".format(defender.name))
        
    end_turn(attacker, defender)
    
while win != True:
    
    if user.active == True:
        os.system('cls||clear')
        print("\nUser's turn!\n")
        print_attacks(user)
        command = ""
        while command not in ["1","2","3"]:
            command = input(command_message)
        do_combat(int(command), user, computer)
        command = input("\nPress any key to continue... ")
        
    if computer.active == True:
        os.system('cls||clear')
        print("\nComputer's turn!\n")
        print_attacks(computer)
        chance = random()
        if computer.health <= 34:
            if chance > 0.3:
                command = 2
            else:
                command = randint(1,3)
        else:
            command = randint(1, 3)
        do_combat(int(command), computer, user)
        input("\nPress any key to continue... ")
