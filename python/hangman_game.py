import sys
from random import randint

WORDS = ("pie", "brown", "sugar", "ham", "cake", "salad")

WRONG_GUESS =   {0:" _____\n |   |\n     |\n     |\n     |\n     |\n     |\n ____|___\n",
                1:" _____\n |   |\n O   |\n     |\n     |\n     |\n     |\n ____|___\n", 
                2:" _____\n |   |\n O   |\n |   |\n     |\n     |\n     |\n ____|___\n", 
                3:" _____\n |   |\n O   |\n/|   |\n     |\n     |\n     |\n ____|___\n", 
                4:" _____\n |   |\n O   |\n/|\  |\n     |\n     |\n     |\n ____|___\n", 
                5:" _____\n |   |\n O   |\n/|\  |\n/    |\n     |\n     |\n ____|___\n", 
                6:" _____\n |   |\n O   |\n/|\  |\n/\\   |\n     |\n     |\n ____|___\n"}

def game():
    
    word_to_guess = WORDS[randint(0, len(WORDS)-1)]
    blanks = {}
    
    for i in range(0, len(word_to_guess)):
        blanks[i] = " __ "
    
    def check_complete():
        blanks_list = []
        
        for value in blanks:
            blanks_list.append(blanks[value])
            
        if ''.join(blanks_list) == word_to_guess:
            print("\n " + ' '.join(blanks_list).upper())
            print("\n " + "YOU WIN!\n")
            play_again()
        else: 
            print("\n " + ' '.join(blanks_list))
    
    def play_again():
        playagain = input("Would you like to play again? >> [y/n] ")
        if playagain.lower() == "y":
            game()
        else:
            sys.exit()
            
    print(WRONG_GUESS[0])
    check_complete()
    
    guesses = 0
    wrong_guesses = 0   
    
    while True:
    
        guess = input("\nEnter a letter or type 'give up' to give up. >> ")
        guess = guess.lower()
        
        if guess.lower() != "quit":
            if guess in word_to_guess:
                indices = [i for i, x in enumerate(word_to_guess) if x == guess]
                for index in indices:
                    blanks[index] = guess
                print(WRONG_GUESS[wrong_guesses])
                check_complete()
                
            else:
                wrong_guesses += 1
                if wrong_guesses <= 6:
                    print(WRONG_GUESS[wrong_guesses])
                    check_complete()
                else: 
                    print("\nGAME OVER\n")
                    print("\nThe word was " + word_to_guess.upper())
                    play_again()
        else:
            print("\nSURRENDERED\n")
            print("\nThe word was " + word_to_guess.upper())
            play_again()
            
game()
