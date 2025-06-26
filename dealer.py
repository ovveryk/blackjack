from cards import deck
from score import calculate_score

def dealer_hit(dealer_cards, counter):

    '''
    Виконується стратегія дилера: бере карти, поки не набере 17 абл більше очок.

    Дилер тягне карти з колоди починаючи з індексу "counter", поки його сума меньша 
    за 17, якщо дилер має 21 в базових картах добір припиняється.

    Args:
        dealer_cards (list): Список карт в колоді 
        counter (int): Індекс поточної карти в колоді, з якого дилер бере карту.

    Returns:
        list: Оновлений список карт дилера.

    '''
    
    game_over = False
    score = calculate_score(dealer_cards)

    if len(dealer_cards) == 2 and score == 22 or score == 21:
        return dealer_cards

    while not game_over:
        if score < 17:
            counter += 1
            dealer_cards.append(deck[counter])
            score = calculate_score(dealer_cards)
        else:
            game_over = True

    return dealer_cards