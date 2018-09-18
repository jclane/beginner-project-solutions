MENU = {"1":3.50, "2":2.50, "3":4.00, "4":3.50, "5":1.75, "6":1.50, "7":2.25, "8":3.75, "9":1.25}

while True:
    total = 0
    order = input(">> ")
    
    for num in order:
        total += MENU[num]
        
    print("TOTAL DUE: ${:,.2f}".format(total))
