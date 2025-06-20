# Hit, Deal, стратегія комп’ютера

from score import calculate_score

def winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if player_score > 21:
        message = "Ти програв! Перебір."
        win = "dealer"
        return message, win
    
    elif dealer_score > 21:
        message = "Ти виграв! Дилер перебрав."
        win = "user"
        return message, win
        
    
    elif player_score == dealer_score:
        message = "Нічия!"
        win = "draw"
        return message, win
    
    elif player_score > dealer_score:
        message = "Ти виграв!"
        win = "user"
        return message, win

    else:
        message = "Ти програв!"
        win = "dealer"
        return message, win