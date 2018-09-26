def recursive():
    
    def whats_my_num(primes, current, i):
    
        if "1" not in str(primes[current]) and "7" not in str(primes[current]):
            sum = 0
            for digit in str(primes[current]):
                sum += int(digit)
            if sum <= 10:
                first = str(primes[current])[0]
                second = str(primes[current])[1]
                last = str(primes[current])[-1]
                if (int(first) + int(second)) % 2 > 0 and int(last) == len(str(primes[current])):       
                    second_to_last = str(primes[current])[1]
                    if int(second_to_last) % 2 == 0 and int(second_to_last) > 1:
                        return primes[current]
        
        return whats_my_num(primes, current + 1, 2)

    primes = []

    for num in range(10, 1000):
        for i in range(2,num + 1):
            if i == num and "1" not in str(num) and "7" not in str(num):
                primes.append(num)
            elif (num % i) == 0:
                break

    print(whats_my_num(primes,0,2))


def do_a_loop():
    primes = []

    for num in range(10,1000 + 1):
        for i in range(2,num + 1):
            if i == num and "1" not in str(num) and "7" not in str(num):
                primes.append(num)
            elif (num % i) == 0:
                break

    less_or_equal = []

    for num in primes:
        sum = 0
        for digit in str(num):
            sum += int(digit)
        if sum <= 10:
            less_or_equal.append(num)
        else:
            continue

    first_and_last = []        

    for num in less_or_equal:
        first = str(num)[0]
        second = str(num)[1]
        last = str(num)[-1]
        if (int(first) + int(second)) % 2 > 0 and int(last) == len(str(num)):
            first_and_last.append(num)
        else:
            continue

    for num in first_and_last:
        second_to_last = str(num)[1]
        if int(second_to_last) % 2 == 0 and int(second_to_last) > 1:
            print(num)

            
print("Using 2 loops and recursion:")
recursive()
print("Using a mess of loops:")
do_a_loop()
