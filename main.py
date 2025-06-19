# Головна функція гри
from score import calculate_score
from cards import deck, closed_card
from hit import hit_card
from game_logic import winner
from dealer import dealer_hit
import random
from tkinter import *


random.shuffle(deck)
print(f"Перемішана колода:\n{deck}")  # Потрібно буде видалити, зараз використовується для тестів
counter = 4
result_messege = None
dealer_hand = deck[:2]
user_hand = deck[2:4]


def end_game():
    btn_hit.configure(state="disabled")
    btn_stand.configure(state="disabled")


def reset_game():
    btn_hit.configure(state="normal")
    btn_stand.configure(state="normal")

    game_result_label.configure(text="")
    player_score_label.configure(text=f"Очки:{calculate_score(user_hand)}")
    player_cards.configure(text=user_hand)


def update_user_hand():
    global user_hand, counter

    if calculate_score(user_hand) < 21:
        user_hand.append(deck[counter])
        counter +=1

        player_score_label.configure(text=f"Очки:{calculate_score(user_hand)}")
        player_cards.configure(text=user_hand)

        if calculate_score(user_hand) > 21:
            end_game()
            game_result_label.configure(text="Перебір")
            return

        return
    
    if calculate_score(user_hand > 21):
        print("Перебір")
        return
    

def start_new_game():
    global counter, dealer_hand,user_hand, deck

    counter = 4
    random.shuffle(deck)
    dealer_hand = deck[:2]
    user_hand = deck[2:4]   

    reset_game()



root = Tk()
root.title("BlackJack")
root.minsize(width=600, height=550)
root.geometry("800x600")
root.configure(bg="#006400")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


header_frame = Frame(root, bg="#006400")
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

main_header = Label(header_frame, text="\u2660 BlackJack \u2660", font=("Helvetica", 28, "bold"), bg="#006400", fg="white")
main_header.pack()


score_frame = Frame(root, bg="#006400")
score_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

player_win = Label(score_frame, text="Гравець: 0", font=("Helvetica", 18), bg="#006400", fg="white")
player_win.pack(side="left", padx=50)

dealer_win = Label(score_frame, text="Дилер: 0", font=("Helvetica", 18), bg="#006400", fg="white")
dealer_win.pack(side="right", padx=50)


separator = Frame(root, height=2, bg="white")
separator.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)


cards_frame = Frame(root, bg="#006400")
cards_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=10)


player_column = Frame(cards_frame, bg='#006400')
player_column.pack(side="left", fill="both",expand=True,padx=20)


dealer_column = Frame(cards_frame, bg='#006400')
dealer_column.pack(side="right",fill="both",expand=True, padx=20)


dealer_cards_label = Label(dealer_column, text="Карти дилера:", font=("Helvetica", 16), bg="#006400", fg="white")
dealer_cards_label.pack(anchor="e", pady=(0, 5))

dealer_cards = Label(dealer_column, text=dealer_hand, font=("Helvetica", 32), bg="#006400", fg="white")
dealer_cards.pack(anchor="e", pady=(0, 20))

dealer_score_label = Label(dealer_column, text="Очки: 32", font=("Helvetica", 16), bg="#006400", fg="white")
dealer_score_label.pack(anchor="e")

player_cards_label = Label(player_column, text="Карти гравця:", font=("Helvetica", 16), bg="#006400", fg="white")
player_cards_label.pack(anchor="w", pady=(0, 5))

player_cards = Label(player_column, text=user_hand, font=("Helvetica", 32), bg="#006400", fg="white")
player_cards.pack(anchor="w", pady=(0, 20))

player_score_label = Label(player_column, text=f"Очки: {calculate_score(user_hand)}", font=("Helvetica", 16), bg="#006400", fg="white")
player_score_label.pack(anchor="w", pady=(0, 20))


buttons_frame = Frame(root, bg="#006400")
buttons_frame.grid(row=4, column=0, columnspan=2, pady=20)

btn_hit = Button(buttons_frame, text="Взяти карту", font=("Helvetica", 14), width=15, bg="#228B22", fg="white", command=update_user_hand)
btn_hit.grid(row=0, column=0, padx=10)

btn_stand = Button(buttons_frame, text="Зупинитись", font=("Helvetica", 14), width=15, bg="#8B0000", fg="white" )
btn_stand.grid(row=0, column=1, padx=10)

btn_new = Button(buttons_frame, text="Нова гра", font=("Helvetica", 14), width=15, bg="#1E90FF", fg="white", command=start_new_game)
btn_new.grid(row=0, column=2, padx=10)

game_result_label = Label(root, text=f"", font=("Helvetica", 20), bg="#006400", fg="white")
game_result_label.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()









# def main():
#     # print(f"Перемішана колода:\n{deck}")  # Потрібно буде видалити, зараз використовується для тестів
#     # print(computer_hand)
#     print("============================")
#     print("Вітаю! Хочеш почати гру в BlackJack? y/n")
#     print("============================")
#     play_game = input("Введи ==>")
#     if play_game.lower() == "n" or play_game.lower() != "y":
#         print("============================")
#         print("Шкода, що не захотіли програти гроші :) ")
#         print("============================")
#         return
    
#     while True:
#         random.shuffle(deck)

#         user_hand = deck[2:4]
#         dealer_hand = deck[:2]
#         calculate_score_user = calculate_score(user_hand)
#         calculate_score_dealer = calculate_score(dealer_hand)
#         print("=========== Карти ==========")
#         print(f"Карти дилера: {dealer_hand[0], closed_card}, в дилера {calculate_score([dealer_hand[0]])} очок \nТвої карти: {user_hand}, в тебе {calculate_score_user} очок ")
#         print("============================")


#         if len(user_hand) == 2 and len(dealer_hand) == 2:

#             if (calculate_score_user == 21 and calculate_score_dealer == 21) or (calculate_score_user == 22 and calculate_score_dealer == 22):
#                     print("=== BlackJack ===")
#                     print("Нічия! Обидва мають BlackJack! ")
#                     print("============================")
#                     print("Хочеш зіграти ще раз? y/n")
#                     print("============================")

#                     new_game = input("Введи ==>")
#                     if new_game.lower() == "n":
#                         print("============================")
#                         print("Дякую за гру! Заходи ще програти гроші :) ")
#                         print("============================")
#                         break
#                     else:
#                         if new_game.lower() == "y":
#                             continue

#             elif calculate_score_user == 22 or calculate_score_user == 21:
#                     print("============================")
#                     print("BlackJack User")
#                     print("============================")
#                     print("Хочеш зіграти ще раз? y/n")
#                     print("============================")
#                     new_game = input("Введи ==>")
#                     if new_game.lower() == "n":
#                         print("============================")
#                         print("Дякую за гру! Заходи ще програти гроші :) ")
#                         print("============================")
#                         break
#                     else:
#                         if new_game.lower() == "y":
#                             continue

#             elif calculate_score_dealer == 22 or calculate_score_dealer == 21:
#                     print("BlackJack Dealer")
#                     print("Хочеш зіграти ще раз? y/n")
#                     print("============================")
#                     new_game = input("Введи ==>")
#                     if new_game.lower() == "n":
#                         print("Дякую за гру! Заходи ще програти гроші :) ")
#                         print("============================")
#                         break
#                     else:
#                         continue


#         user_hand = hit_card(user_hand)

#         dealer_hit(dealer_hand)
#         winner(user_hand, dealer_hand)
#         print(f"Твої карти {user_hand} \nКарти дилера:{dealer_hand}")
#         print("============================")
#         print("Хочеш зіграти ще раз? y/n")
#         print("============================")
#         new_game = input("Введи ==>")

#         if new_game.lower() == "n":
#             print("============================")
#             print("Дякую за гру! Заходи ще програти гроші :) ")
#             print("============================")
#             break

# main()







