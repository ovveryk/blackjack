# Функції підрахунку очок, calculate_score
from constants import CARD_NAMES

def calculate_score(hand):

    calc = 0
    aces = 0

    for card in hand:
        value = CARD_NAMES.get(card, 0)
        calc += value
        if value == 11:
            aces += 1

    while calc > 21 and aces > 0:
        calc -= 10
        aces -= 1

    return calc