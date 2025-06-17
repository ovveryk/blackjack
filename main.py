# Головна функція гри
from score import calculate_score
from cards import deck, closed_card
from hit import hit_card
from game_logic import winner
from dealer import dealer_hit
import random


def main():
    # print(f"Перемішана колода:\n{deck}")  # Потрібно буде видалити, зараз використовується для тестів
    # print(computer_hand)
    print("============================")
    print("Вітаю! Хочеш почати гру в BlackJack? y/n")
    print("============================")
    play_game = input("Введи ==>")
    if play_game.lower() == "n" or play_game.lower() != "y":
        print("============================")
        print("Шкода, що не захотіли програти гроші :) ")
        print("============================")
        return
    
    while True:
        random.shuffle(deck)

        user_hand = deck[2:4]
        dealer_hand = deck[:2]
        calculate_score_user = calculate_score(user_hand)
        calculate_score_dealer = calculate_score(dealer_hand)
        print("=========== Карти ==========")
        print(f"Карти дилера: {dealer_hand[0], closed_card}, в дилера {calculate_score([dealer_hand[0]])} очок \nТвої карти: {user_hand}, в тебе {calculate_score_user} очок ")
        print("============================")


        if len(user_hand) == 2 and len(dealer_hand) == 2:

            if (calculate_score_user == 21 and calculate_score_dealer == 21) or (calculate_score_user == 22 and calculate_score_dealer == 22):
                    print("=== BlackJack ===")
                    print("Нічия! Обидва мають BlackJack! ")
                    print("============================")
                    print("Хочеш зіграти ще раз? y/n")
                    print("============================")

                    new_game = input("Введи ==>")
                    if new_game.lower() == "n":
                        print("============================")
                        print("Дякую за гру! Заходи ще програти гроші :) ")
                        print("============================")
                        break
                    else:
                        if new_game.lower() == "y":
                            continue

            elif calculate_score_user == 22 or calculate_score_user == 21:
                    print("============================")
                    print("BlackJack User")
                    print("============================")
                    print("Хочеш зіграти ще раз? y/n")
                    print("============================")
                    new_game = input("Введи ==>")
                    if new_game.lower() == "n":
                        print("============================")
                        print("Дякую за гру! Заходи ще програти гроші :) ")
                        print("============================")
                        break
                    else:
                        if new_game.lower() == "y":
                            continue

            elif calculate_score_dealer == 22 or calculate_score_dealer == 21:
                    print("BlackJack Dealer")
                    print("Хочеш зіграти ще раз? y/n")
                    print("============================")
                    new_game = input("Введи ==>")
                    if new_game.lower() == "n":
                        print("Дякую за гру! Заходи ще програти гроші :) ")
                        print("============================")
                        break
                    else:
                        continue


        user_hand = hit_card(user_hand)

        dealer_hit(dealer_hand)
        winner(user_hand, dealer_hand)
        print(f"Твої карти {user_hand} \nКарти дилера:{dealer_hand}")
        print("============================")
        print("Хочеш зіграти ще раз? y/n")
        print("============================")
        new_game = input("Введи ==>")

        if new_game.lower() == "n":
            print("============================")
            print("Дякую за гру! Заходи ще програти гроші :) ")
            print("============================")
            break

main()







