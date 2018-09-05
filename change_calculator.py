from decimal import Decimal, ROUND_HALF_UP

COINS = {"quarters":Decimal('0.25'), "nickles":Decimal('0.05'), "dimes":Decimal('0.10'), "pennies":Decimal('0.01')}

def round_decimal(x):
  return x.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

while True:
    coins_due = []
    
    def get_coins(coin):
        global num
        count = 0
        result = Decimal('0.00')
        while result < num:
            result = result + Decimal(COINS[coin])
            count += 1
            
            if result == num:
                num -= Decimal(COINS[coin]) * count
                return count
            elif result > num:
                count -= 1
                result = result - Decimal(COINS[coin])
                num -= Decimal(COINS[coin]) * count
                return count

    tendered = Decimal(input("\nEnter amount tendered >> "))
    price = Decimal(input("\nEnter price of item >> "))
    
    num = round_decimal(tendered - price)

    quarters = get_coins("quarters")
    dimes = get_coins("dimes")
    nickles = get_coins("nickles")
    pennies = get_coins("pennies")
    
    print("\nChange due:")
    print("\n\tQuarter: " + str(quarters))
    print("\tDimes:   " + str(dimes))
    print("\tNickles: " + str(nickles))
    print("\tPennies: " + str(pennies))
