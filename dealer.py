from cards import deck
from score import calculate_score

def dealer_hit(dealer_cards, counter):
    
    game_over = False
    score = calculate_score(dealer_cards)

    if len(dealer_cards) == 2 and score == 22 or score == 21:
        return dealer_cards

    while not game_over:
        if score < 17:
            counter += 1
            dealer_cards.append(deck[counter])
            score = calculate_score(dealer_cards)
        else:
            game_over = True

    return dealer_cards