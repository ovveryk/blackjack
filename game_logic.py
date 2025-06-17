# Hit, Deal, стратегія комп’ютера

from score import calculate_score

def winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print("\n===== Результат раунду =====")
    print(f"Твої очки: {player_score}, \nОчки дилера: {dealer_score}")
    print("============================")

    if player_score > 21:
        print("Ти програв! Перебір. ")
        print("============================")
        return
    elif dealer_score > 21:
        print("Ти виграв! Дилер перебрав. ")
        print("============================")
        return
    elif player_score == dealer_score:
        print("Нічия! ")
        print("============================")
        return
    elif player_score > dealer_score:
        print("Ти виграв! ")
        print("============================")
        return
    else:
        print("Ти програв! ")
        print("============================")
        return