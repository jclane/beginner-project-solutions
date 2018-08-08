import sys, os
from random import randint

while True:
    OPTIONS = {1:"rock", 2:"paper", 3:"scissors"}
    score_player = 0
    score_computer = 0

    def did_player_win(player_move, computer_move):

        if OPTIONS[player_move] == "rock" and computer_move != "paper":
            return True
        else:
            return False
            
        if OPTIONS[player_move] == "paper" and computer_move != "rock":
            return True
        else:
            return False
            
        if OPTIONS[player_move] == "scissors" and computer_move != "rock":
            return True
        else:
            return False
    
    def menu():
        os.system('cls')
        print("Welcome to ROCK_PAPER_SCISSORS!\n")
        
        if score_player > 0 or score_computer > 0:
            print("\tCurrent Scores")
            print("\t----------------")
            print("\tPlayer  : {}".format(score_player))
            print("\tComputer: {}\n".format(score_computer))
        
        for el in OPTIONS:
            print(str(el)+'.', OPTIONS[el])
            
        the_game()

    def the_game():
        global score_computer, score_player
        while True:
            try:
                player_move = int(input("\nMake your move! >> "))
                if not player_move > len(OPTIONS) and not player_move < 1:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\n\n!ERROR : Please select a number from the menu.')
                continue   
        
        computer_move = OPTIONS[randint(1,3)]

        print("\nYou chose {}".format(OPTIONS[player_move]))
        print("The computer chose {}".format(computer_move))
        
        if OPTIONS[player_move] == computer_move:
            print("\nDRAW!")
        else:
            if did_player_win(player_move, computer_move):
                score_player += 1
                print("\nYou WIN!")
            else:
                score_computer += 1
                print("\nYou LOSE!")
        
        play_again = input("\nWould you like to play again? >> ")
        if play_again.lower() == 'y' or play_again.lower() == "yes":
            menu()
        else:
            raise SystemExit()
    
    menu()
