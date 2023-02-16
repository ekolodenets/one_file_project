import os
import random
import time

# seed 4 with aces
# random.seed(87) - BJ
# random.seed(87)

MONEY = 1000
BET = 10
DECK = []
WAIT = 2

def make_card_deck():
    global DECK
    titles = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
              'A': 11}
    suit = ['♣️', '♦️', '♥️', '♠️']
    cards = [[k, i, v] for i in suit for k, v in titles.items()]
    random.shuffle(cards)
    DECK = cards


def hands(*args):
    aces = len([i[0] for i in args if i[0] == 'A'])
    hand = [f'{a}{b}' for a, b, c in args]
    score = sum([c for a, b, c in args])
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return hand, score


def pick_a_card():
    global DECK
    card = DECK.pop()
    return card


def prnt(ph, dh, open=False):
    os.system('cls')
    print(f'{MONEY=}, {BET=}', '\n')
    d_h, d_s = hands(dh[0]) if not open else hands(*dh)
    print(f'Dealer hand: {" ".join(d_h)}', f'Dealer scores: {d_s}', sep='\n')
    print()
    p_h, p_s = hands(*ph)
    print(f'Your hand: {" ".join(p_h)}', f'Your scores: {p_s}', sep='\n')


def dealer_hand(player, dealer):
    os.system('cls')
    prnt(player, dealer, True)
    points = hands(*dealer)[1]
    if points < 17:
        time.sleep(WAIT)
        dealer.append(pick_a_card())
        dealer_hand(player, dealer)
    elif points > 21 or points < hands(*player)[1]:
        global MONEY
        MONEY += BET * 2
        print(f'You won ${BET * 2}')
    else:
        print('You lost')
    time.sleep(WAIT)
    start_game()


def player_hand(player, dealer):
    points = hands(*player)[1]
    if points > 21:
        print('You lost')
        time.sleep(WAIT)
        start_game()
    elif points == 21:
        print("Dealer's turn")
        time.sleep(WAIT)
        dealer_hand(player, dealer)
    else:
        inp = input('1 - pick one more card, 2 - pass: ')
        if inp == '1':
            player.append(pick_a_card())
            prnt(player, dealer)
            player_hand(player, dealer)

        else:
            print("Dealer's turn")
            time.sleep(WAIT)
            dealer_hand(player, dealer)


def first_hand():
    global MONEY
    MONEY -= BET
    player = []
    dealer = []
    player.append(pick_a_card())
    dealer.append(pick_a_card())
    player.append(pick_a_card())
    dealer.append(pick_a_card())
    prnt(player, dealer)
    if sum([c for a, b, c in player]) == 21:
        prize = int(BET * 3.5)
        print('Congratulations!!! You have a BLACK JACK!!!')
        print('You won', prize)
        MONEY += prize
        time.sleep(WAIT)
        start_game()
    else:
        player_hand(player, dealer)


def start_game():
    if MONEY > 0:
        while True:
            os.system('cls')
            print(f'{MONEY=}', '\n')
            bet = int(input('How much you want to bet? '))
            if bet > MONEY:
                print("You don't have so much!")
            else:
                global BET
                BET = bet
                first_hand()
                break


make_card_deck()
start_game()
print('Goodbye, thanks for playing')