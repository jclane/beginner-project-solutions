COIN_TYPES = {1:('penny', 'pennies'), 2:('nickle', 'nickles'), 3:('dime', 'dimes'), 4:('quarter', 'quarters')}
COIN_WEIGHTS = {1:2.50, 2:5, 3:2.268, 4:5.67}
COIN_ROLLS = {1:50, 2:40, 3:50, 4:40}
COIN_VALUES = {1:0.01, 2:0.05, 3:0.10, 4:0.25}

user_total = []

def get_totals(coin_type, weight):
    total = weight / COIN_WEIGHTS[coin_type]
    wrappers_needed = total / COIN_ROLLS[coin_type]
    value = total * COIN_VALUES[coin_type]
    
    return [coin_type, str(round(total)), str(round(wrappers_needed)), value]

def show_results():
    if len(user_total) > 0:
        for el in user_total:
            print("\nTotal {coin}:".format(coin = COIN_TYPES[el[0]][0] if el[1] == 1 else COIN_TYPES[el[0]][1])) 
    
while True:

    coins_type = print("\nCoins by weight:")

    print("\n\t1. Penny")
    print("\t2. Nickle")
    print("\t3. Dime")
    print("\t4. Quarter")
    print("\t5. Show me the money!")

    coins_type = int(input("\nEnter [1-4] >> "))
    
    if coins_type != 5:
        coins_weight = float(input("Enter total weight for coins of this type >> "))
        user_total.append(get_totals(int(coins_type), coins_weight))
    else:
        show_results()
