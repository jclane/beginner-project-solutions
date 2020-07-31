from random import choice
from sys import exit
import os

FACE_CARDS = {14:"Ace", 13:"King", 12:"Queen", 11:"Jack"}

DECK_OF_CARDS = {14:(4, 1), 13:(4, 10), 12:(4, 10), 11:(4, 10), 10:(4, 10),
                9:(4, 9), 8:(4, 8), 7:(4, 7), 6:(4, 6), 5:(4, 5), 4:(4, 4), 
                3:(4, 3), 2:(4, 2), 1:(4, 1)}

class Deck:
    def __init__(self, cards):
        self.cards = cards
        
    def deal(self):

        card = choice(list(self.cards))
        while self.cards[card][0] == 0:
            card = choice(list(self.cards))
        if card in user_hand.cards:
            user_hand.cards[card] += 1
        else:
            user_hand.cards[card] = 1            
        print("\n{} dealt to user.\n".format(card if card not in FACE_CARDS else FACE_CARDS[card]))
        self.cards[card] = self.cards[card][0] - 1, self.cards[card][1]
                    
class Hand:
    def __init__(self, cards, hand_value):
        self.cards = cards
        self.hand_value = 0
        
    def show(self):
        print("Current hand\n")
        print(" # | Card")
        print("_________")
        for card in self.cards:
            print("{:>2} | {}{}".format(self.cards[card], 
                  card if card not in FACE_CARDS else FACE_CARDS[card], 
                  's' if self.cards[card] > 1 else ''))
        self.total()
  
    def total(self):
        total = 0
        for card in self.cards:
            total += DECK_OF_CARDS[card][1]
        self.hand_value = total
        if self.hand_value > 21:
            print("BUST!")
        else: 
            print("\nYou're currently at: {}".format(self.hand_value))
        
class Round:
    def __init__(self, game_score):
        self.number = 1
        self.game_score = 100
        
    def end(self):
        self.number += 1
        self.round_score = 21 - user_hand.hand_value
        self.game_score = self.game_score - self.round_score
        if self.number == 5:

            if self.game_score <= 59:
                game_rank = "F"
            elif self.game_score <= 69:
                game_rank = "D"
            elif self.game_score <= 79:
                game_rank = "C"
            elif self.game_score <= 89:
                game_rank = "B"
            elif self.game_score <= 100:
                game_rank = "A"
            
            print("\nGAME SCORE: ", self.game_score)
            print("RANK: ", game_rank)
            exit()
        else:
            input("Press any key to continue...")
            
round = Round(100)     
user_hand = Hand({}, 0)

while round.number < 5:
    the_deck = Deck(DECK_OF_CARDS)        
    os.system('cls||clear')
    print("Round: {}\n".format(round.number))
    
    if round.number == 1:
        the_deck.deal()
        the_deck.deal()
        user_hand.show()
    
    deal_or_hold = ""
    while deal_or_hold not in ["d", "h", "q"]:
        deal_or_hold = input("\nDeal or hold? >> [d/H/Quit] ")
    
    if deal_or_hold.lower() == "d":
        the_deck.deal()
        user_hand.show()
        round.end()
    elif deal_or_hold.lower() == "h":
        user_hand.show()
        round.end()
    elif deal_or_hold.lower() == "q" or deal_or_hold.lower() == "quit":
        print("\nQuitting...")
        exit()
