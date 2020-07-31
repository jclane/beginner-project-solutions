import sys

def loop_fibonacci(n):
    sequence = []
    count = n
    num1 = 0
    num2 = 1
    i = 1;
    while (i < count):
        result = num1 + num2
        num1 = num2
        num2 = result
        sequence.append(result)
        i += 1
    
    return sequence[-1]

def recursive_fibonacci(n):
    if (n < 2):
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
 
while True: 
    loop_or_rescursive = input("Use loop method or rescursive method? >> [enter 'l' or 'r'] ")
    
    if (loop_or_rescursive.lower() == 'r'):
        response = input("Enter a number or 'q' to quit >> ")
        if (response.lower() != 'q'):
            print(recursive_fibonacci(int(response)))
        else:
            System.exit()
    if (loop_or_rescursive.lower() == 'l'):
        response = input("Enter a number or 'q' to quit >> ")
        if (response.lower() != 'q'):
            print(loop_fibonacci(int(response)))
        else:
            System.exit()
