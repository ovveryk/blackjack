# Головна функція гри
from score import calculate_score
from cards import deck, closed_card
from hit import hit_card
from game_logic import winner
from dealer import dealer_hit


play_game = ""

def main():
    print(f"Перемішана колода:\n{deck}")  # Потрібно буде видалити, зараз використовується для тестів
    # print(computer_hand)

    print("Вітаю! Хочеш почати гру? y/n")


    play_game = input()
    if play_game == "y":
        print(play_game)
        user_hand = deck[2:4]
        dealer_hand = deck[:2]
        calculate_score_user = calculate_score(user_hand)
        calculate_score_dealer = calculate_score(dealer_hand)
        print(user_hand, dealer_hand, calculate_score_user, calculate_score_dealer)


        # Додати перевірку на нічію

        if len(user_hand) == 2 and calculate_score_user == 22 or calculate_score_user == 21:
            print("BlackJack User") #Додати логіку
        if len(dealer_hand) == 2 and calculate_score_dealer == 22 or calculate_score_dealer == 21:
            print("BlackJack Dealer") #Додати логіку


        user_hand = (hit_card(user_hand))
        print(user_hand)

        dealer_hit(dealer_hand)
        winner(user_hand, dealer_hand)

    if play_game == "n":
        print("Шкода, що не захотіли програти гроші :)")

main()













# Для імпорта функцій робимо так:
#     Припустимо, у тебе є файл math_utils.py з такою функцією:
#
#     def add(a, b):
#         return a + b
#
# Ти можеш імпортувати і використати її так:
# В файлі де вона потрібна пишемо так:
#     from math_utils import add
#
#  А потім її викликаємо:
#    result = add(2, 3)
#    print(result)  # 5