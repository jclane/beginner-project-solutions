from sys import exit
from random import randrange
from re import match


def roll_die(amount, sides):
    rolls = []
    for i in range(0, amount):
        roll = rolls.append(randrange(1, sides + 1))
       
    for roll in rolls:
        values.append(roll)
        
    return rolls 
    
def validate_input(to_validate):
    for item in to_validate:
        if not match(r"[\d?]+d[\d]+", item):
            return False
        else:
            return True
            
    return False

D6 = {1:" _______\n|       |\n|   O   |\n|_______|\n", 2:" _______\n|O      |\n|       |\n|______O|\n",
      3:" _______\n|      O|\n|   O   |\n|O______|\n", 4:" _______\n|O     O|\n|       |\n|O_____O|\n",
      5:" _______\n|O     O|\n|   O   |\n|O_____O|\n", 6:" _______\n|O     O|\n|O     O|\n|O_____O|\n"}
    
while True:
    values = []
    results = {}
    die_rolls = {}
    response = ""
    total_value = 0
    
    while validate_input(response) == False:
        print("\nEnter the type and number of dice you would like to roll [ex. 2d6]")
        print("Multiple requests can be seperated by a space [ex. 1d4 2d6 3d8 1d100]")
        response = input(">> ")
        response = response.split(" ")
    
    for item in response:
        params = item.split("d")
        die_rolls[item] = roll_die(int(params[0]), int(params[1]))
        
    for item in response:     
        print("\n{}:".format(item))    
        for roll in die_rolls[item]:
            if item.endswith("d6"):
                print("{}".format(D6[roll]))
            else:
                print("  {}".format(roll))

    for value in values:
        results[value] = values.count(value)
        total_value += value
        
    print("\nNum  | Number of occurances and percentage\n{}".format("-" * 42))
    
    results = sorted(results.items())
    
    for ndx in range(0, len(results)):
        print("{:<4} | {} times or {:.00%} of the time".format(results[ndx][0], results[ndx][1], results[ndx][1] / len(values)))
    
    print("\nTotal of all dice rolls: {}".format(str(total_value)))
    
    response = input("\nRoll again? [y/N] >> ")
    
    if response.lower() == 'n':
        exit()
