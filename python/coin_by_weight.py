import sys

COIN_TYPES = {1:('penny', 'pennies'), 2:('nickle', 'nickles'), 3:('dime', 'dimes'), 4:('quarter', 'quarters')}
COIN_WEIGHTS = {"g":{1:2.50, 2:5, 3:2.268, 4:5.67}, "lbs":{1:0.0055115565546, 2:0.011023113109, 3:0.0050000841064, 4:0.012698626302}}
COIN_ROLLS = {1:50, 2:40, 3:50, 4:40}
COIN_VALUES = {1:0.01, 2:0.05, 3:0.10, 4:0.25}

user_total = []

def get_totals(coin_type, weight_measure, weight):
    total = weight / COIN_WEIGHTS[weight_measure][coin_type]
    wrappers_needed = total / COIN_ROLLS[coin_type]
    value = total * COIN_VALUES[coin_type]
    
    return [coin_type, str(round(total)), str(round(wrappers_needed)), value]

def show_results():
    sum_total = 0
    if len(user_total) > 0:
        for el in user_total:
            print("\nTotal {coin}: {coins}".format(coin = COIN_TYPES[el[0]][0] if el[1] == 1 else COIN_TYPES[el[0]][1], coins = el[1]))
            print("Wrappers Needed: {}".format(el[2]))
            print("Value: ${:,.2f}".format(el[3]))
        
        for el in user_total:
            sum_total += el[3]
        
        print("\nCombined Value: ${:,.2f}".format(sum_total))
        run_again = input("\nWould you like to calculate more coins by weight? Enter [y/n] ")
        if run_again.lower() == "n" or run_again.lower() == "no": sys.exit()

while True:

    coins_type = print("\nCoins by weight:")

    print("\n\t1. Penny")
    print("\t2. Nickle")
    print("\t3. Dime")
    print("\t4. Quarter")
    print("\t5. Show me the money!")
    print("\t6. Quit")
    
    coins_type = int(input("\nEnter [1-6] >> "))
    
    while coins_type not in range(1,6):
        print("\nInvalid entry. Please try again.")
        coins_type = int(input("\nEnter [1-6] >> "))
    
    if coins_type >= 1 and coins_type <= 4:
        weight_measure = input("\nWould you like to enter weight in grams or pounds? Enter [g or lbs] >> ")
        coins_weight = float(input("Enter total weight for coins of this type >> "))
        user_total.append(get_totals(int(coins_type), weight_measure, coins_weight))
    elif coins_type == 5:
        show_results()
    elif coins_type == 6:
        sys.exit()
