"""
This Program Creates The Deck Shuffles it and return the card
"""

from card import *
import random


class Deck:
    # The __init__ function create a deck in order
    def __init__(self):
        self.all_cards = []

        for skin in card_skin:
            for rank in card_rank:
                self.all_cards.append((rank, skin))

    # This function returns a shuffled deck
    def shuffle(self):
        random.shuffle(self.all_cards)
        return self.all_cards
