COINS = {"quarters":.25, "nickles":.05, "dimes":.10, "pennies":.01}

while True:
    coins_due = []
    
    def get_coins(coin):
        global num
        count = 0
        result = 0
        while result < num:
            result += COINS[coin]
            count += 1
            
            if result == num:
                num -= COINS[coin] * count
                return count
            elif result > num:
                count -= 1
                result -= COINS[coin]
                num -= COINS[coin] * count
                return count

        

    num = float(input("\nEnter change due >> "))

    quarters = get_coins("quarters")
    dimes = get_coins("dimes")
    nickles = get_coins("nickles")
    pennies = get_coins("pennies")
    
    print("\nChange due:")
    print("\n\tQuarter: " + str(quarters))
    print("\tDimes: " + str(dimes))
    print("\tNickles: " + str(nickles))
    print("\tPennies: " + str(pennies))
