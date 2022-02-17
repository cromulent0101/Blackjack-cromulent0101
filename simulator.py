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
decks = 6
chips = 100    
hands = []


def play_specific_cards_once(cards:list,action,dealer_card): 
    """
    Takes in a list of cards and plays ONE action on them versus the dealer. Bet will always be 10
    """
    # create a deck specifically for this one hand
    deck = []
    for i in range(decks):
        deck.extend([i for i in range(0,51)])               # will add ability for multi-deck
    random.shuffle(deck)

    if action.startswith("h"):
        cards.extend(dealCard(deck))
    elif action.startswith("st"):
        pass  # leave the loop of betting for this hand
    elif action.startswith("d"): 
        cards.extend(dealCard(deck))
    
    if cards.getHandValue > 21:
        print(f"Player busts! ({hand.value})")
        return -10
    elif cards.getHandValue == 21:
        return 15
    else:



 # deck should be shuffled and we sequentially remove cards from list using pop

# deck = [5,6]  # dealyer's cards
# # deck.extend([3,3,4,3,5,3,3,3,8,9,7,11,12,13,3,3,4]) # players cards
# deck.extend([3,2,3,5,5,5]) # players cards

while(chips > 0):
    bet = 10

    holeCard = dealCard(deck) # hidden from players/dealer but if hole card is an ace, dealer checks
    faceUpCard = dealCard(deck) # visible to player

    # create player's hand
    pHand = Hand([],bet,False)
    chips -= bet
    pHand.dealCard(deck)
    pHand.dealCard(deck)

    # create dealer's hand
    dHand = [faceUpCard,holeCard]
    print(f"Dealer card:   {cardMap[faceUpCard]}")


    if pHand.value==21 and getHandValue(dHand)[0]==21: # blackjack push
        pHand.printPlayerHand()
        print(f"Push!")
        chips += bet

    elif getHandValue(dHand)[0]==21:     # dealer blackjack
        printDealerHand(dHand)
        print("Dealer blackjack!")

    elif pHand.value==21:    # if player gets blackjack they instantly win 1.5 value of their bet
        pHand.printPlayerHand()
        print("Player blackjack!")
        chips += round(bet*(5/2))
    else: 
        playHand(pHand,False,1)

        playable_hands = []
        # print("Dealer is now dealing...")
        while (getHandValue(dHand)[0] < 17): 
            dHand.append(dealCard(deck))
            if getHandValue(dHand)[0] == 17 and getHandValue(dHand)[1] and s17: break
        
        print("")
        for hand in hands:
            if hand.value < 21:
                playable_hands.append(hand)
        if playable_hands:
            printDealerHand(dHand)
        # i = 1
        for hand in playable_hands:
            hand.printPlayerHand()
            # print(f"this is hand {i}")
            i += 1
            if hand.value > 21: 
                print(f"Player busts! ({hand.value})")
            else:
                if getHandValue(dHand)[0] > 21:
                    print(f"Dealer busts! ({getHandValue(dHand)[0]})")
                    chips += hand.b*2
                    continue
                if hand.value > getHandValue(dHand)[0]:
                    print(f"Player ({hand.value}) beats dealer ({getHandValue(dHand)[0]})!")
                    chips += hand.b*2
                elif (hand.value < getHandValue(dHand)[0]) and (getHandValue(dHand)[0] < 22): # dealer can still get BJ here
                    print(f"Dealer ({getHandValue(dHand)[0]}) beats player ({hand.value})!")
                else:
                    print(f"Push! ({getHandValue(dHand)[0]})")
                    chips += hand.b
    hands = []
    print("Chips: ",chips)
    