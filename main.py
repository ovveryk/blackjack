# Головна функція гри
from score import calculate_score
from cards import deck, closed_card
from game_logic import winner
from dealer import dealer_hit
import random
from tkinter import *


random.shuffle(deck)
deck_index = 4
result_messege = None
dealer_hand = deck[:2]
user_hand = deck[2:4]
player_score = 0
dealer_score = 0


def end_game():
    """
    Завершує гру, оновлюючи стан кнопок у графічному інтерфейсі.

    Вимикає кнопки "Взяти карту" (btn_hit) і "Зупинитися" (btn_stand), 
    щоб запобігти подальшим діям гравця, та активовує кнопку  
    "Нова гра" (btn_new), дозволяючи почати нову гру.

    Returns:
        None
    """
    btn_hit.configure(state="disabled")
    btn_stand.configure(state="disabled")
    btn_new.configure(state="normal")
    


def dealer_first_card():
    '''
    Роздає першу карту дилера, приховуючи другу карту і рахує очки 
    тільки відкритої карти.

    Оновлює інтерфейс:
        - Відображає першу карту дилера.
        - Приховує другу карту, використовується зміна "closed_card".
        - Відображаються очки лише відкритої карти за допомогою функціх "calculate_score".
     
    Returns:
        None
    '''
    dealer_cards.configure(text=[dealer_hand[0], closed_card])
    dealer_score_label.configure(text=f"Очки: {calculate_score([dealer_hand[0]])}")


def dealer_full_cards():
    '''
    Роздає всі карти дилера, рахуючи очки всіх карт.

    Оновлює інтерфейс:
        - Відображає всі карти дилера
        - Відображає очки всіх карт дилера за допомогою функції "calculate_score".

    Returts:
        None
    '''
    dealer_cards.configure(text=dealer_hand)
    dealer_score_label.configure(text=f"Очки: {calculate_score(dealer_hand)}")


def reset_game():
    '''
    Скидає стан гри до початкового та оновлює інтерфейс.

    Вмикає кнопки "Взяти карту" та "Зупинитися", а кнопку "Нова гра" вимикає, 
    щоб запобігти передчасному перезапуску. Очищає поле з результатом гри, 
    оновлює карти гравця та дилера, і викликає функцію `dealer_first_card()` 
    для відображення початкового стану дилера.

    Оновлює інтерфейс:
        - Увімкнення/вимкнення кнопок.
        - Скидання тексту результату гри.
        - Відображення нових карт гравця.
        - Запуск першого ходу дилера.

    Returns:
        None
    
    '''
    btn_hit.configure(state="normal")
    btn_stand.configure(state="normal")
    btn_new.configure(state="disabled")

    game_result_label.configure(text="")
    player_score_label.configure(text=f"Очки:{calculate_score(user_hand)}")
    player_cards.configure(text=user_hand)
    dealer_first_card()


def update_user_hand():
    '''
    Додає нову карту гравцю, оновлює інтерфейс та перевіряє перебір.

    Якщо сума очок гравця не перевищує 21, функція додає наступну карту з колоди 
    до руки гравця, оновлює кількість очок та відображає нову руку. 

    Якщо після добору сума очок перевищує 21:
        - Гра завершується викликом `end_game()`.
        - Виводиться повідомлення "Перебір".
        - Дилер отримує одне очко.
        - Відображається повна рука дилера.

    Залежності:
        - Використовує глобальні змінні: `user_hand`, `deck_index`, `dealer_score`, `deck`.
        - Оновлює елементи інтерфейсу: `player_score_label`, `player_cards`, `game_result_label`, `dealer_win`.
        - Викликає зовнішні функції: `calculate_score()`, `end_game()`, `dealer_full_cards()`.

    Returns:
        None
    '''
    global user_hand, deck_index, dealer_score

    if calculate_score(user_hand) <= 21:
        user_hand.append(deck[deck_index])
        deck_index += 1

        player_score_label.configure(text=f"Очки:{calculate_score(user_hand)}")
        player_cards.configure(text=user_hand)

        if calculate_score(user_hand) > 21:
            end_game()
            
            game_result_label.configure(text="Перебір", fg="red")
            dealer_score += 1
            dealer_win.configure(text=f"Дилер: {dealer_score}")
            dealer_full_cards()
            return

        return
    
    
def update_dealer_hand():

    '''
    Оновлює руку дилера, обчислює результ та завершує гру.

    Виконує:
        - Викликає "dealer_hit()", для добору карт дилером.
        - Оновлює інтерфейс: карти дилера, очки, повна рука.
        - Перевіряє наявність BlackJack у дилера.
        - Використовує "winner()" для визначення переможця.
        - Ононвлює рахунок в залежності від переможця.
        - Виводить повідомлення про результат гри.
    
    Глобальні змінні:
        dealer_hand (list): карти дилера. 
        deck_index (int): індекс поточної карти в колоді.
        dealer_score (int): кількість перемог дилера.
        player_score (int): кількість перемог гравця.
        user_hand (list): карти гравця.

    Returns: 
        None
         
    '''

    global dealer_hand, deck_index, dealer_score, player_score, user_hand
    dealer_hand = dealer_hit(dealer_hand, deck_index)
    d_score = calculate_score(dealer_hand)
    dealer_full_cards()

    dealer_cards.configure(text=dealer_hand)
    dealer_score_label.configure(text=f"Очки: {calculate_score(dealer_hand)}")

    if d_score == 21 and len(dealer_hand) == 2:
        dealer_score += 1
        game_result_label.configure(text="BlackJack! Дилер виграв!", fg="red")
        dealer_win.configure(text=f"Дилер: {dealer_score}")
        end_game()
        return
    
    message, win = winner(user_hand, dealer_hand)

    if win == "dealer":

        dealer_score += 1
        game_result_label.configure(text=message, fg="red")
        dealer_win.configure(text=f"Дилер: {dealer_score}")
        end_game()
        return

    if win == "draw":
         dealer_full_cards()
         game_result_label.configure(text="Нічия", fg="white")
         end_game()
         return
    
    if win == "user":
         
        player_score += 1
        game_result_label.configure(text=message, fg="#00FF00")
        player_win.configure(text=f"Гравець: {player_score}")  
        end_game()
        return
    
    return

def blackjack_new():

    '''
    Перевіряє BlackJack на початковій роздачі, як у гравця так і у дилера.

    Перевіряє такі випадки:
        - Обидва мають BlackJack
        - Гравець має BlackJack, автоматична перемога гравця.
    
    Якщо хоч один з цих випадків підходить, гра завершується ("end_game()"),
    виводится відповідне повідомлення на екран, оновлюється рахунок, виводяться всі 
    карти дилерра ("dealer_full_cards()").

    Глобальні змінні: 
    global dealer_hand (list): карти дилера
    user_hand (list): карти гравця
    player_score (int): рахунок гравця
    dealer_score (int): рахунок дилера

    Returns:
        bool: True, якщо виявлено BlackJack або  нічия з BlackJack.
              False, якщо гра триває.  

    '''

    global dealer_hand, user_hand, player_score, dealer_score

    pl_score = calculate_score(user_hand)
    d_score = calculate_score(dealer_hand)

    if pl_score == 21 and d_score == 21 and len(user_hand) == 2 and len(dealer_hand) == 2:
        end_game()
        dealer_full_cards()
        game_result_label.configure(text="Нічия! Обидва мають BlackJack!", fg="white")
        return True

    elif pl_score == 21 and len(user_hand) == 2:
        end_game()
        dealer_full_cards()
        game_result_label.configure(text="BlackJack! Ти виграв!", fg="#00FF00")
        player_score += 1
        player_win.configure(text=f"Гравець: {player_score}")
        return True
    
    return False


def start_new_game():

    '''
    Запускає нову гру BlackJack, ініціалізує колоду, роздає карти та оновлює інтерфейс.

    Виконує наступні зміни: 
        - Перемішує колоду (deck)
        - Роздає по дві карти гравцю та дилеру.
        - Скидає інтерфейс (reset_game()) 
        - Оновлення відображення карт і очок дилера
        - Перевіряє на початку BlackJack (blackjack_new())
        - Якщо гравець або обидва мають BlackJack, показує карти дилера і показує очки.

    Глобальні змінні:
        counter (int):
        dealer_hand (list):
        user_hand (list):
        deck (list):
        deck_index (int):

    Returns: 
        Nonep.
    '''

    global counter, dealer_hand,user_hand, deck, deck_index

    deck_index = 4
    random.shuffle(deck)
    dealer_hand = deck[:2]
    user_hand = deck[2:4]   

    reset_game()

    player_score_label.configure(text=f"Очки: {calculate_score(user_hand)}")
    player_cards.configure(text=user_hand)

    if blackjack_new():
        dealer_score_label.configure(text=f"Очки: {calculate_score(dealer_hand)}")
        dealer_cards.configure(text=dealer_hand)

blackjack_new()

# === Ініціалізація вікна ===
root = Tk()
root.title("BlackJack")
root.minsize(width=1200, height=700)
root.geometry("1200x700")
root.configure(bg="#003300")

# === Налаштування сітки ===
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(10, weight=0)

# === Заголовок ===
header_frame = Frame(root, bg="#003300")
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

main_header = Label(header_frame, text="\u2660 BlackJack \u2660", font=("Helvetica", 28, "bold"), bg="#003300", fg="white")
main_header.pack()

# === Рахунок гравця та дилера ===
score_frame = Frame(root, bg="#003300")
score_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

player_win = Label(score_frame, text="Гравець: 0", font=("Helvetica", 25), bg="#003300", fg="white")
player_win.pack(side="left", padx=50)

dealer_win = Label(score_frame, text="Дилер: 0", font=("Helvetica", 25), bg="#003300", fg="white")
dealer_win.pack(side="right", padx=50)

# === Роздільник ===
separator = Frame(root, height=2, bg="white")
separator.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

# === Секція з картами ===
cards_frame = Frame(root, bg="#003300")
cards_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=70)

# === Колонка гравця ===
player_column = Frame(cards_frame, bg='#003300')
player_column.pack(side="left", fill="both",expand=True,padx=20)

# === Колонка дилера ===
dealer_column = Frame(cards_frame, bg='#003300')
dealer_column.pack(side="right",fill="both",expand=True, padx=20)

# === Карти дилера ===
dealer_cards_label = Label(dealer_column, text="Карти дилера:", font=("Helvetica", 25), bg="#003300", fg="white")
dealer_cards_label.pack(anchor="e", pady=(0, 5))

dealer_cards = Label(dealer_column, text=dealer_hand, font=("Helvetica", 90), bg="#003300", fg="white")
dealer_cards.pack(anchor="e", pady=(0, 20))

dealer_score_label = Label(dealer_column, text=f"Очки: {calculate_score(dealer_hand)}", font=("Helvetica", 25), bg="#003300", fg="white")
dealer_score_label.pack(anchor="e")

# === Карти гравця ===
player_cards_label = Label(player_column, text="Карти гравця:", font=("Helvetica", 25), bg="#003300", fg="white")
player_cards_label.pack(anchor="w", pady=(0, 5))

player_cards = Label(player_column, text=user_hand, font=("Helvetica", 90), bg="#003300", fg="white")
player_cards.pack(anchor="w", pady=(0, 20))

player_score_label = Label(player_column, text=f"Очки: {calculate_score(user_hand)}", font=("Helvetica", 25), bg="#003300", fg="white")
player_score_label.pack(anchor="w", pady=(0, 20))

# === Кнопки керування грою === 
buttons_frame = Frame(root, bg="#D9D6C7")
buttons_frame.grid(row=10, column=0, columnspan=2, sticky = "ew", pady=(10, 0))

btn_hit = Button(buttons_frame, text="Взяти карту", font=("Helvetica", 14), width=15, bg="#228B22", fg="white", command=update_user_hand)
btn_hit.pack(side="left", padx=40, pady=10, expand=True)

btn_stand = Button(buttons_frame, text="Зупинитись", font=("Helvetica", 14), width=15, bg="#8B0000", fg="white", command=update_dealer_hand)
btn_stand.pack(side="left", padx=40, pady=10, expand=True)

btn_new = Button(buttons_frame, text="Нова гра", font=("Helvetica", 14), width=15, bg="#1E90FF", fg="white", command=start_new_game)
btn_new.pack(side="left", padx=40, pady=10, expand=True)

# === Вивід результату гри ===
game_result_label = Label(root, text=f"", font=("Helvetica", 20), bg="#003300", fg="white")
game_result_label.grid(row=5, column=0, columnspan=2, pady=20)

btn_new.configure(state="disabled")
dealer_first_card()
root.mainloop()



