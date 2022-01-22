import random
import time
from cardutils import getHandValue,printDealerHand,convertNonAceCard,cardMap,dealCard,Hand

## settings ##
ddas = True
s17 = False
surrender = False
onlySplitPairs = False
decks = 1
chips = 100

def playHand(hand: Hand, split: bool): 
    if hand.s: hand.dealCard()          # if this hand is a product of split, deal another card
    global hands
    global chips
    if hand.value == 21: 
        hand.printPlayerHand()
        hands.append(hand)
        print("Player blackjack!")
    while hand.value < 21:              # play blackjack! only give player options when value below 21
        hand.printPlayerHand()
        action = input("Hit, stand, double, or split? ").lower()
        if action.startswith("h"):
            hand.dealCard()
        elif action.startswith("st"):
            hands.append(hand)
            break  # leave the loop of betting for this hand
        elif action.startswith("d"): # and ddas is allowed...
            if (len(hand.c) == 2) and (ddas or not hand.s):  # only allow doubles on two cards
                hand.dealCard()
                chips -= hand.b
                hand.b += hand.b
                hands.append(hand)
                break
            else: print("Not a valid move")
        elif action.startswith("sp"): # splits can only happen when a hand has two cards
            if onlySplitPairs:
                if hand.c[0] != hand.c[1]:
                    print("You can't split non-pairs") # at some casinos you can split face cards
                else:
                    playHand(Hand([pHand.c[0]],hand.b,True),True)
                    chips -= hand.b
                    playHand(Hand([pHand.c[1]],hand.b,True),True)
                    break
            else:
                if convertNonAceCard(hand.c[0]) != convertNonAceCard(hand.c[1]):
                    print("You can't split cards of different values") # at some casinos you can split face cards
                else:
                    playHand(Hand([pHand.c[0]],hand.b,True),True)
                    chips -= hand.b
                    playHand(Hand([pHand.c[1]],hand.b,True),True)
                    break
        else:
            print("Not a valid move")
        if hand.value > 21:
            hand.printPlayerHand()
            print(f"Player bust! ({hand.value})!")
            hands.append(hand)
        if hand.value == 21:
            hand.printPlayerHand()
            hands.append(hand)
            print("Player blackjack!")


deck = []
for i in range(decks):
    deck.extend([i for i in range(0,51)])               # will add ability for multi-deck
random.shuffle(deck) # deck should be shuffled and we sequentially remove cards from list using pop

deck = [2,3]  # dealyer's cards
deck.extend([3,3,4,3,5,3,3,3,8,9,10,11,12,13,3,3,4]) # players cards

while(chips > 0):
    bet = int(input("Enter your bet: "))

    holeCard = dealCard(deck) # hidden from players/dealer but dFaceUp is an ace, dealer checks
    faceUpCard = dealCard(deck) # visible to player

    # create player's hand
    pHand = Hand([],bet,False)
    chips -= bet
    pHand.dealCard(deck)
    pHand.dealCard(deck)

    # create dealer's hand
    dHand=[faceUpCard,holeCard]
    print(f"Dealer card:   {cardMap[faceUpCard]}")

    hands = []

    if pHand.value==21 and getHandValue(dHand)[0]==21: # blackjack push
        pHand.printPlayerHand()
        print(f"Push!")

    elif getHandValue(dHand)[0]==21:     # dealer blackjack
        printDealerHand(dHand)
        print("Dealer blackjack!")

    elif pHand.value==21:    # if player gets blackjack they instantly win 1.5 value of their bet
        pHand.printPlayerHand()
        print("Player blackjack!")
        chips += bet*(5/2)
    else: 
        playHand(pHand,False)
        # print("Dealer is now dealing...")
        while (getHandValue(dHand)[0] < 17): 
            dHand.append(dealCard(deck))
            if getHandValue(dHand)[0] == 17 and getHandValue(dHand)[1] and s17: break
        printDealerHand(dHand)

        for hand in hands:
            hand.printPlayerHand()
            if hand.value > 21: 
                print(f"Player busted! ({hand.value})")
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


    print("Chips: ",chips)
    