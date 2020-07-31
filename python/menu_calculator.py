from sys import exit
from os import system


MENU = {"1":("Chicken Strips", 3.50), "2":("French Fries", 2.50), "3":("Hambuger", 4.00),
        "4":("Hotdog", 3.50), "5":("Large Drink", 1.75), "6":("Medium Drink", 1.50), 
        "7":("Milk Shake", 2.25), "8":("Salad", 3.75), "9":("Small Drink", 1.25)}

while True:
    total = 0
    order_counts = {}
    
    print("\nMENU:\n")

    for item in MENU:
        print("{}. {:<16} ${:<16,.2f}".format(item, MENU[item][0], MENU[item][1]))

    order = input("\n>> ")
    
    for num in order:
        count = 0
        total += MENU[num][1]
        order_counts[num] = order.count(num)
        
    print("\nOrder Summary:\n")

    for count in order_counts:
        print("\t" + str(order_counts[count]), MENU[count][0])
    
    
    print("\nTOTAL DUE: ${:,.2f}\n".format(total))
    response = input("New order? >> [Y/n] ")
    if response.lower() == "n":
        exit()
    else:
        system('cls||echo -e \\\\033c')
