from constants import CARD_NAMES
'''
Рахує суму очок у руці.

Усі карти мають значення відповідно до словника "CARD_NAMES"
Тузи можуть мати значення 1 або 11 в залежності від загальної суми, 
якщо сума меньша за 21, значення - 11, більша за 21 - 1.

Args:
    hand(list): список карт у руці у вигляді символів.

Returns:
    int: Загальна сума очок в руці з урахуванням зменьшеної вартості тузів при переборі.

'''
def calculate_score(hand):

    calc = 0
    aces = 0

    for card in hand:
        value = CARD_NAMES.get(card, 0)
        calc += value
        if value == 11:
            aces += 1

    while calc > 21 and aces > 0:
        calc -= 10
        aces -= 1

    return calc
