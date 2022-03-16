"""
This is a blackjack game
Min Bet amount is 500
"""

import time
from deck import *
from player import *
import os

# Create a dealer and human
dealer = Player('Dealer', 100)
human = Player('Player 1', 500)


# Clear the Console
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


clear_console()


# Display card in hand
def show_card(hand):
    for face, rank in hand:
        card = Cards(face, rank)
        print(card, end=' ')


# blackjack hit
def hit(player):
    # Show Card and Total of Dealer if a human is playing
    if player.name != 'Dealer':
        print('Dealer Card:', end=' ')
        show_card(dealer.hand)
        print(f'\nDealer Total: {dealer.total()}')
    # Add one card to current player
    player.add_card(deck.pop(0))

    # Show Card and total of current player
    print(f'\n{player.name} Card:', end=' ')
    show_card(player.hand)
    print(f'\n{player.name} Total: {player.total()}')
    # If current player total is greater than 20, exit
    if player.total() >= 21:
        return True

    # If a human player want to hit or stand
    if player.name != 'Dealer':
        print('\n1) Hit')
        print('2) Stand')
        while True:
            # loop until correct value is provided
            try:
                hit_or_stand = int(input('Enter 1 or 2: '))
                if hit_or_stand not in range(1, 3):
                    raise ValueError
                break
            except ValueError:
                pass
    # If Current player is the Dealer
    else:
        # if Dealers total is greater than human total stand, else hit
        if dealer.total() > human.total():
            hit_or_stand = 2
        else:
            hit_or_stand = 1
    # If current player chose to hit
    if hit_or_stand == 1:
        clear_console()
        print(f'Bet Placed:{bet}                           Token Remaining:{human.token}')
        return False
    # If current player chose to stand
    return True


def game():
    # Give one card to human and dealer
    dealer.add_card(deck.pop(0))
    human.add_card(deck.pop(0))
    stand = False
    # Check if player chose to hit or stand
    while not stand:
        stand = hit(human)
    # Check if human score is 21 or greater
    # If human players total is greater than 21 is a bust, player lost
    if human.score > 21:
        print('BUST')
        return 'lose'
    # if human players score is equal to 21 if Blackjack, player won
    elif human.score == 21:
        print('Blackjack')
        return 'win'
    else:
        stand = False
        # The dealer plays
        while not stand:
            stand = hit(dealer)

    # Check if player won or lost
    if dealer.total() > 21:
        return 'win'
    elif dealer.total() == 21 or (dealer.total() > human.total()):
        return 'lose'
    elif dealer.total() < human.total():
        return 'win'
    else:
        return 'draw'


game_over = False


while not game_over:
    print(f'Token Remaining:{human.token}\n')
    # Place the bet
    if human.token >= 500:
        print('Bet amount must be divisible by 500')
        print('Enter Min for minimum value (500) and All for All In')

        while True:
            # loop until correct value is entered
            try:
                bet = input('Place your bet: ').lower()
                if bet == 'min':
                    bet = 500

                elif bet == 'all':
                    bet = human.token
                else:
                    bet = int(bet)

                if bet % 500 == 0:
                    if bet == 0:
                        game_over = True
                        print('+ Until next time.\n+ Bye')
                        time.sleep(10)
                        clear_console()
                        break
                    else:
                        if human.token >= bet:
                            human.place_bet(bet)
                            break
                        else:
                            print('\nNot Enough Tokens')
                            raise ValueError
                else:
                    print('Invalid Bet')
                    raise ValueError
            except ValueError:
                pass
    else:
        print('Not enough token to play')
        game_over = True
    if not game_over:
        clear_console()
        print(f'Bet Placed:{bet}                           Token Remaining:{human.token}')

        # Create a deck
        global deck
        deck = Deck()
        deck = deck.shuffle()
        # victory returns a winner after game is over
        victory = game()
        clear_console()
        print('Dealer Card:', end=' ')
        show_card(dealer.hand)
        print(f'\nDealer Total: {(dealer.total())}')
        print(f'\n{human.name} Card:', end=' ')
        show_card(human.hand)
        print(f'\n{human.name} Total: {human.total()}')
        # Doubles the bet amount if won
        if victory == 'win':
            print('\nCongrats, You Won !!!!!\n')
            human.add_token(bet * 2)
        # Receives bet amount if it's a draw
        elif victory == 'draw':
            print('\nIts a Draw\n')
            human.add_token(bet)
        # Do nothing if lost
        else:
            print('\nThe Dealer Won\n')

        # Asks whether the user wants to play again
        print(f'Token Remaining: {human.token}')
        print('1) Play Again')
        print('2) Quit')
        while True:
            try:
                play_again = int(input('Enter 1 or 2: '))
                if play_again not in range(1, 3):
                    raise ValueError
                break
            except ValueError:
                pass
        if play_again == 1:
            # resets everything if player wants to play again
            clear_console()
            human.reset()
            dealer.reset()
        else:
            game_over = True
            print('+ Until next time.\n+ Bye')
            time.sleep(1)
            clear_console()
