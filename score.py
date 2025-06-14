# Функції підрахунку очок, calculate_score
from constants import CARD_NAMES

def calculate_score(hand):


    calc = 0
    aces = 0

    for card in hand:
        for suit in ['\u2660', '\u2665', '\u2666', '\u2663']:
            card = card.replace(suit, '')

        calc += CARD_NAMES.get(card, 0)

        if card == 'A':
            aces += 1

    while calc > 21 and aces > 0:
        calc -= 10
        aces -= 1

    return calc