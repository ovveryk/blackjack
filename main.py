# Головна функція гри
from score import calculate_score
from cards import deck, closed_card
from hit import hit_card

user = True
computer_hand = hit_card()


def main():
    print(f"Перемішана колода:\n{deck}")  # Потрібно буде видалити, зараз використовується для тестів
    print(computer_hand)


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