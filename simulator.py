import random
import time
from cardutils import getHandValue,printDealerHand,convertNonAceCard,cardMap,Hand,dealCard,convertNonAceCard
from strategy import split_strat, strat, my_strat

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
    deck.remove(dealer_card-1)
    # remove one of the dealer's card from the deck
    dealer_cards = [dealer_card, dealCard(deck)]
    if getHandValue(dealer_cards)[0] == 21: return -10

    while True:
        if action.startswith("h"):
            cards.append(dealCard(deck))
            if getHandValue(cards)[0] < 21:
                value,soft = getHandValue(cards)
                action = my_strat[(value,soft,convertNonAceCard(dealer_card))]
                if action == 'double':
                    action = 'hit'
                if not action: break
                continue
            break
        elif action.startswith("st"):
            break  # leave the loop of betting for this hand
        elif action.startswith("d"): 
            cards.append(dealCard(deck))
            double = 2
            break

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

cards_to_test = [10,10] # how can I pass this by value
trials = 500
up_card = 1
hit_chips = 10000
for i in range(trials):
    hit_chips += play_specific_cards_once([10,10],"hit",up_card)
print(hit_chips)
double_chips = 10000
for i in range(trials):
    double_chips += play_specific_cards_once([10,10],"double",up_card)
print(double_chips)
stand_chips = 10000
for i in range(trials):
    stand_chips += play_specific_cards_once([10,10],"stand",up_card)
print(stand_chips)