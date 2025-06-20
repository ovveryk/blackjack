# Hit, Deal, стратегія комп’ютера

from score import calculate_score

def winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if player_score > 21:
        return "Ти програв! Перебір.", "dealer"
    
    elif dealer_score > 21:
        return "Ти виграв! Дилер перебрав.", "user"
    
    elif player_score == dealer_score:
        return "Нічия!", "draw"
    
    elif player_score > dealer_score:
        return "Ти виграв!", "user"
    
    else:
        return "Ти програв!", "dealer"