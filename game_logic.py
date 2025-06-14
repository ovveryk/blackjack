# Hit, Deal, стратегія комп’ютера

from score import calculate_score

def winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print(f"Твої очки: {player_score}, Очки дилера: {dealer_score}")

    if player_score > 21:
        print("Ти програв! Перебір. ")
        return
    elif dealer_score > 21:
        print("Ти виграв! Дилер перебрав. ")
        return
    elif player_score == dealer_score:
        print("Нічия! ")
        return
    elif player_score > dealer_score:
        print("Ти виграв! ")
        return
    else:
        print("Ти програв! ")
        return