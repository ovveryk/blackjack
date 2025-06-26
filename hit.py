def hit_card( user_cards, counter, deck):
    '''
    Додає одну карту до руки гравця з колоди та збільшує лічильник.

    Функція бере карту з колоди за індексом `counter`, додає її до списку 
    карт гравця (`user_cards`) та повертає оновлену руку і нове значення лічильника.

    Args:
        user_cards (list): Список карт гравця.
        counter (int): Індекс поточної карти в колоді.
        deck (list): Повна колода карт, з якої відбувається роздача.

    Returns:
        tuple: 
            list — оновлений список карт гравця,
            int — нове значення лічильника (counter + 1).
    '''
    
    user_cards.append(deck[counter])
    counter +=1

    return user_cards, counter
  

      
     
         

