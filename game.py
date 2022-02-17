import random
import time
from cardutils import getHandValue,printDealerHand,convertNonAceCard,cardMap,Hand,dealCard
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


def playHand(hand: Hand, split: bool, j: int): 
    if hand.s: hand.dealCard(deck)          # if this hand is a product of split, deal another card
    if True: # debug
        hand.printPlayerHand()
        print(f"this is the {j} time playing a hand")
        print(f"This hand is a split: {hand.s}")
    j += 1
    global hands
    global chips
    if hand.value == 21: 
        hand.printPlayerHand()
        hands.append(hand)
        print("Player blackjack!")
    while hand.value < 21:              # play blackjack! only give player options when value below 21
        hand.printPlayerHand()
        time.sleep(1)
        action = input("Hit, stand, double, or split? ").lower()
        # get the correct action for this hand
        if(len(hand.c)==2 and hand.c[0] == hand.c[1]):
            correct_action = split_strat[(hand.c[0],faceUpCard)]
        else:
            correct_action = strat[(hand.value,hand.soft,faceUpCard)]

        if action.startswith("h"):
            if(correct_action=="Hit"):
                print("Correct choice!")
            else:
                print(f"Wrong, you should have {correct_action}")
            hand.dealCard(deck)
        elif action.startswith("st"):
            if(correct_action=="Stand"):
                print("Correct choice!")
            else:
                print(f"Wrong, you should have {correct_action}")
            hands.append(hand)
            break  # leave the loop of betting for this hand
        elif action.startswith("d"): # and ddas is allowed...
            if(correct_action=="Double"):
                print("Correct choice!")
            else:
                print(f"Wrong, you should have {correct_action}")
            if (len(hand.c) == 2) and (ddas or not hand.s):  # only allow doubles on two cards
                chips -= hand.b
                hand.b += hand.b
                hand.dealCard(deck)
                hand.printPlayerHand()
                if hand.value > 21:
                    print(f"Player busts! ({hand.value})")
                if hand.value == 21:
                    print("Player blackjack!")
                    time.sleep(1)
                hands.append(hand)
                break
            else: print("Not a valid move")
        elif action.startswith("sp"): # splits can only happen when a hand has two cards
            if(correct_action=="Split"):
                print("Correct choice!")
            else:
                print(f"Wrong, you should have {correct_action}")
            if onlySplitPairs:
                if hand.c[0] != hand.c[1]:
                    print("You can't split non-pairs") # at some casinos you can split face cards
                else:
                    playHand(Hand([pHand.c[0]],hand.b,True),True,j)
                    chips -= hand.b
                    playHand(Hand([pHand.c[1]],hand.b,True),True,j)
                    break
            else:
                if convertNonAceCard(hand.c[0]) != convertNonAceCard(hand.c[1]):
                    print("You can't split cards of different values") # at some casinos you can split face cards
                else:
                    playHand(Hand([pHand.c[0]],hand.b,True),True,j)
                    chips -= hand.b
                    playHand(Hand([pHand.c[1]],hand.b,True),True,j)
                    break
        else:
            print("Not a valid move")
        if hand.value > 21:
            hand.printPlayerHand()
            print(f"Player busts! ({hand.value})")
            hands.append(hand)
        if hand.value == 21:
            hand.printPlayerHand()
            hands.append(hand)
            print("Player blackjack!")
            time.sleep(1)


deck = []
for i in range(decks):
    deck.extend([i for i in range(0,51)])               # will add ability for multi-deck
random.shuffle(deck) # deck should be shuffled and we sequentially remove cards from list using pop

# deck = [2,3]  # dealyer's cards
# deck.extend([3,3,4,3,5,3,3,3,8,9,7,11,12,13,3,3,4]) # players cards
# deck.extend([9,10,11,12,13,13,12,11,10]) # players cards


while(chips > 0):
    while True:
        try:
            bet = int(input("Enter your bet: "))
            break
        except ValueError:
            print("Invalid bet")
    if bet < 1 or bet > chips:
        print("Invalid bet")
        continue

    holeCard = dealCard(deck) # hidden from players/dealer but dFaceUp is an ace, dealer checks
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
        # print("Dealer is now dealing...")
        while (getHandValue(dHand)[0] < 17): 
            dHand.append(dealCard(deck))
            if getHandValue(dHand)[0] == 17 and getHandValue(dHand)[1] and s17: break
        
        print("")
        printDealerHand(dHand)
        i = 1
        for hand in hands:
            hand.printPlayerHand()
            print(f"this is hand {i}")
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

    print("Chips: ",chips)
    