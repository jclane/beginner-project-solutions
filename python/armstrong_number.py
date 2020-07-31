def get_input():
    valid_num = False
    while not valid_num:
        user_input = input("Please enter a number:\n")
        valid_num = user_input.isnumeric()
    
    return user_input
    
def is_armstrong(num):
    n = len(num)
    if n == 1:
        return True
    
    result = 0
    for d in map(int, num):
        result += pow(d, n)

    return int(result) == int(num)

def test():
    num = get_input()
    print(is_armstrong(num))
    
test()
