import sys

n = 9

def make_table(n):
    print("\n    MULTIPLICATION TABLE: 1-{}\n".format(n))
    for row in range(1, n + 1):
        print(*(f"{row*col:3}" for col in range(1, n + 1)))
              
make_table(n)        
        
while True:
    
    request = "\nPlease enter a number or 'q' to quit >> "
    n = input(request)
    
    try:
        make_table(int(n))
    except ValueError:
        if n.lower() == "q": 
            print("\nGoodbye")
            sys.exit()
