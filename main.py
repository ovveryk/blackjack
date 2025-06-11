# Головна функція гри
from score import calculate_score
from cards import deck, closed_card

def main():
    print(f"Перемішана колода:\n{deck}")  # Потрібно буде видалити, зараз використовується для тестів

    computer_hand = deck[:2]
    hand = deck[2:4]

    print(f"\nДилер: {computer_hand[0]} {closed_card}", f"\nТвої карти: {hand[0]} {hand[1]}", )
    score = calculate_score(hand)
    print(f"Твої очки {score}")

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