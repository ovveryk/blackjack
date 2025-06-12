# Логіка тягнення карт
from cards import deck
from score import calculate_score



def hit_card():
    user_cards = deck[2:4]
    counter = 4
    game_over = False
    score = calculate_score(user_cards)

    if len(user_cards) == 2 and score == 22 or score == 21:
        return user_cards

    while not game_over:

        user_deal = input("Введіть 'Y', щоб взяти карту, або 'N' щоб зупинитися: ")
        if user_deal == "y":
            counter +=1
            user_cards.append(deck[counter])
            print(deck[counter])

        else:
            game_over = True

    return user_cards

