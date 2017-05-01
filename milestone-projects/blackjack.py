#Milestone Project 2 - Blackjack Game In this milestone project you will be creating a Complete BlackJack Card Game in Python.
# Here are the requirements:
# You need to create a simple text-based BlackJack game

# The game needs to have one player versus an automated dealer.

#Deck 
# 2-10 are face value
# Face cards are worth 10
# Aces are worth 1 or 11

#Hand/Rules
# Starts with 2 cards, 
# Can ask for additional cards 
# 21 Points is a win

# Player Class
# The player can stand or hit.
# The player must be able to pick their betting amount.
# You need to keep track of the players total money.
# You need to alert the player of wins, losses, or busts, etc...

import random

class Player(object):
    def __init__(self, bankroll):
        self.bankroll = bankroll

    def __str__(self):
        return 'Player has entered the game with $%s' %(self.bankroll)

    def add_to_bankroll(self, amount):
        return self.bankroll + amount

class Deck(object):
    card_values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    card_suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']    


class Hand(Deck):
    def __init__(self):
        Deck.__init__(self)
    
    def player_start(self):
        starting_hand = ()
        while len(starting_hand) < 2:
            card1 = random.choice(Deck.card_values) + ' ' + 'of' + ' ' + random.choice(Deck.card_suits)
            card2 = random.choice(Deck.card_values) + ' ' + 'of' + ' ' + random.choice(Deck.card_suits)
            starting_hand = (card1, card2)
        self.hand_value(starting_hand)
        return starting_hand
        

    def table_start(self):
        starting_hand = ()
        while len(starting_hand) < 2:
            card1 = random.choice(Deck.card_values) + ' ' + 'of' + ' ' + random.choice(Deck.card_suits)
            card2 = random.choice(Deck.card_values) + ' ' + 'of' + ' ' + random.choice(Deck.card_suits)
            starting_hand = (card1, card2)
        self.hand_value(starting_hand)
        return starting_hand

    # def hit():

    def hand_value(self, starting_hand):
        hand_length = len(starting_hand)
        card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12 = starting_hand


        if card1.find('2') != -1:
            card1_value = 2;
            print(card1_value)
            return card1_value

        # print(starting_hand[0])
        


player_hand = Hand()
table_hand = Hand()
print(player_hand.player_start())
print(table_hand.table_start())
# print(player_hand.check_win())
# print(table_hand.check_win())

# play_blackjack = input('Would you like to play blackjack? (y/n) ').upper()
# if play_blackjack == 'Y':
#     player = Player(100)
# else:
#     print('Come back some other time')
#     exit()
# print(player)


