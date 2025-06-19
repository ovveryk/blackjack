# Логіка тягнення карт

from score import calculate_score


def hit_card( user_cards, counter, deck):
    
    user_cards.append(deck[counter])
    counter +=1

    return user_cards, counter
  

      
     
         

