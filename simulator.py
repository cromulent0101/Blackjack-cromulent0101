import random
import time
from cardutils import getHandValue,printDealerHand,convertNonAceCard,cardMap,Hand,dealCard,convertNonAceCard
from strategy import split_strat, strat

debug: False

## settings ##
ddas = True
s17 = False     # Does dealer stand on soft 17?
surrender = False
onlySplitPairs = False
decks = 2
chips = 100    
hands = []


def play_specific_cards_once(cards:list,action,dealer_card): 
    """
    Takes in a list of cards and plays ONE action on them versus the dealer. Bet will always be 10
    """
    # create a deck specifically for this one hand
    double = 1
    deck = []
    for i in range(decks):
        deck.extend([i for i in range(0,51)])               # will add ability for multi-deck
    random.shuffle(deck)
    # print(deck)
    deck.remove(dealer_card-1)
    # print(deck)
    # remove one of the dealer's card from the deck
    dealer_cards = [dealer_card, dealCard(deck)]
    if getHandValue(dealer_cards)[0] == 21: return -10

    # print(dealer_cards)

    if action.startswith("h"):
        cards.append(dealCard(deck))
    elif action.startswith("st"):
        pass  # leave the loop of betting for this hand
    elif action.startswith("d"): 
        cards.append(dealCard(deck))
        double = 2
    if getHandValue(cards)[0] > 21:
        return -10*double
    elif getHandValue(cards)[0] == 21:
        return 15*double
    else:
        while (getHandValue(dealer_cards)[0] < 17): 
            dealer_cards.append(dealCard(deck))
            if getHandValue(dealer_cards)[0] == 17 and getHandValue(dealer_cards)[1] and s17: break
    
    if getHandValue(dealer_cards)[0] > 21: return 10*double
    elif getHandValue(dealer_cards)[0] > getHandValue(cards)[0]: return -10*double
    elif getHandValue(dealer_cards)[0] == getHandValue(cards)[0]: return 0
    else: return 10*double

print(play_specific_cards_once([10,5],"hit",5))

hit_chips = 1000
for i in range(100000):
    hit_chips += play_specific_cards_once([5,6],"hit",1)
print(hit_chips)
stand_chips = 1000
for i in range(100000):
    stand_chips += play_specific_cards_once([5,6],"double",1)
print(stand_chips)