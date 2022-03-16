"""
This Program assigns each card to a number
In blackjack only rank of the card is important, Skin is ignored.
K, Q, J value is 10
Ace can be 1 or 11 as per players wish
"""

card_skin = ("Spades", "Clubs", "Hearts", "Diamonds")
card_rank = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
face_cards = ('Jack', 'Queen', 'King')
card_value = {}

# assigning each card to a number
for i in range(2, 11):
    card_value[card_rank[i - 2]] = i

# Assign k,q,j to 10
for card in face_cards:
    card_value[card] = 10


class Cards:

    def __init__(self, rank, skin):
        self.rank = rank
        self.skin = skin

        # If rank is an Ace do not give a value(Value of ace is assigned on spot)
        if rank == 'Ace':
            pass
        else:
            # If not ace, then assign a rank
            self.value = card_value[rank]

    def __str__(self):
        # A print statement will give the below value
        return f'{self.rank} of {self.skin}'


