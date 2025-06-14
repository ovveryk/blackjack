# Логіка тягнення карт
from cards import deck
from score import calculate_score



def hit_card( user_cards):
    counter = 3
    game_over = False
    score = calculate_score(user_cards)
    while not game_over:

        user_deal = input("Введіть 'Y', щоб взяти карту, або 'N' щоб зупинитися: ")
        if user_deal == "y":
            counter +=1
            user_cards.append(deck[counter])
            score = calculate_score(user_cards)
            print(f"Твоя карта: [{deck[counter]}],\nТвої карти {user_cards} маєш {score} очок")
            if score > 21:
                print("Перебір, Ти програв! :(")
                game_over = True

        else:
            game_over = True

    return user_cards

