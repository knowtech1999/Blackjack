"""
This program give Every player an empty hand
"""
from card import *


class Player:
    # __init__ Takes a name, value and tokens
    def __init__(self, name, token):
        self.name = name
        self.hand = []
        self.token = token
        self.score = 0  # This is total of all cards
        self.in_hand = []  # Temporary hand for calculating total

    # Place the bet
    def place_bet(self, bet):
        self.token -= bet

    # Deposit the token won
    def add_token(self, token):
        self.token += token

    # Add card to self.hand
    def add_card(self, card):
        self.hand.append(card)
        self.in_hand.append(card)

    # Calculate the total of all cards
    def total(self):
        # loop through self.hand
        for cards in self.in_hand:
            # Create a card object
            card = Cards(cards[0], cards[1])
            # Check if rank is an ace
            if cards[0] == 'Ace':
                # Check if the player ia a human player
                if self.name != 'Dealer':
                    while True:
                        try:
                            # Ask Human player to assign an ace value
                            value = int(input("\nDo you want ace value to be 1 or 11: "))
                            # loop until player give a correct value
                            if value != 1 and value != 11:
                                raise ValueError
                            else:
                                self.score += value
                                break
                        except ValueError:
                            pass
                # If dealer gets an ace and total is less than 10 then ace value is 11 else ace value is 1
                else:
                    if self.score <= 10:
                        self.score += 11
                    else:
                        self.score += 1
            # Card not an ace
            else:
                self.score += card.value
        # clear self in hand
        self.in_hand = []
        return self.score
    # reset hand and score
    def reset(self):
        self.hand = []
        self.score = 0

    def __str__(self):
        return f'{self.name} has {self.token} left'
