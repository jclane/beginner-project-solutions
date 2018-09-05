import sys
from random import randint

num = randint(1,100)
guesses = 0

print("High or Lower: The Number Guessing Game")
print("\nHOW TO PLAY:")
print("\n\t* I have selected a number between 1 and 100.")
print("\t* You must input a number in an effort to guess the number I have selected.")
print("\t* If the number you have guessed is too lower, I will tell you.")
print("\t* Likewise, if the number is too high, I will also tell you that.")

while True:

    def select_num():
        num = randint(1,100)
        return num
    
    try:
        guess = int(input("\nEnter guess >> "))
    except ValueError:
        guess = int(input("Enter numbers only >> " ))

    if guess == 1984:
        print(num)
    elif guess < num:
        guesses += 1
        print("Too low!")
    elif guess > num:
        guesses += 1
        print("Too high!")
    elif guess == num:
        guesses += 1
        print("\nYou guessed it!  And it only took you {} tries! Great job!".format(guesses))
        keepplaying = input("Would you like to play again? [y/n] >> ")
        if keepplaying.lower() == "n":
            print("Goodbye")
            sys.exit()
        elif keepplaying.lower() == "y":
            select_num()
