# Головна функція гри
from score import calculate_score
from cards import deck, closed_card
from hit import hit_card
from game_logic import winner
from dealer import dealer_hit


def main():
    # print(f"Перемішана колода:\n{deck}")  # Потрібно буде видалити, зараз використовується для тестів
    # print(computer_hand)

    print("Вітаю! Хочеш почати гру? y/n")


    play_game = input()
    if play_game == "y":
        user_hand = deck[2:4]
        dealer_hand = deck[:2]
        calculate_score_user = calculate_score(user_hand)
        calculate_score_dealer = calculate_score(dealer_hand)
        print(user_hand, dealer_hand)
        print(calculate_score_user, calculate_score_dealer)


        if len(user_hand) == 2 and len(dealer_hand) == 2:

            if (calculate_score_user == 21 and calculate_score_dealer == 21) or (calculate_score_user == 22 and calculate_score_dealer == 22):
                print("Нічия! Обидва мають BlackJack! ") #Додати логіку

            elif calculate_score_user == 22 or calculate_score_user == 21:
                print("BlackJack User") #Додати логіку

            elif calculate_score_dealer == 22 or calculate_score_dealer == 21:
                print("BlackJack Dealer") #Додати логіку


        user_hand = (hit_card(user_hand))
        print(user_hand)

        dealer_hit(dealer_hand)
        winner(user_hand, dealer_hand)

    if play_game == "n":
        print("Шкода, що не захотіли програти гроші :) ")

main()









