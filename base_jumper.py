import sys


def convert_num(num, new_base):
    convertString = "0123456789abcdef"
    if num < new_base:
      return convertString[int(num)]
    else:
      return convert_num(num / new_base, new_base) + convertString[int(num % new_base)]
      
def limit(num):
    return num < 2 or num > 16
        
while True:
    num = input("Please enter an integer to convert >> ")
        
    base = input("Please enter the current base of the integer [2-16] >> ")
    
    while limit(int(base)) != False:
        base = input("Please enter a number between 2 and 16 >> ")

    new_base = input("Please enter the base you would like to convert to [2-16] >> ")    
        
    while limit(int(new_base)) != False:
        new_base = input("Please enter a number between 2 and 16 >> ")
        
    if base != "10":
        result = int(num, int(base))
        print(str(result))
    else:
        print(convert_num(int(num), int(new_base)))
        
    response = input("Would you like to convert another number? [y/n] >> ")
    
    if response.lower() == 'n':
        sys.exit()
