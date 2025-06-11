# Логіка карт (draw_card, назви карт, тощо)
import random

deck = []

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", 'J', 'Q', 'K', 'A']
suits = ['\u2660', '\u2665', '\u2666', '\u2663']
closed_card = '\U0001F0A0'

for suit in suits:
    for rank in ranks:
        deck.append(rank+suit)

random.shuffle(deck)