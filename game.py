import random
import time
from cardutils import getHandValue,printDealerHand,convertNonAceCard,cardMap,Hand,dealCard,convertNonAceCard
from strategy import split_strat, strat

DEBUG = False

''' settings '''
ddas = True             # Can you double down after a split?
s17 = False             # Does dealer stand on soft 17?
surrender = False       # TODO: implement surrender
onlySplitPairs = False
decks = 6
chips = 100    
hands = []


def playHand(hand: Hand, split: bool, j: int) -> None:
    ''' 
    Main loop for the sim.

    Given a Hand, play Blackjack until you win, lose, or push.
    '''
    if hand.split: hand.dealCard(deck)          # if this hand is a product of split, deal another card
    if DEBUG: # debug
        hand.printPlayerHand()
        print(f"this is the {j} time playing a hand")
        print(f"This hand is a split: {hand.split}")
        j += 1
    # global hands # don't know if we need this
    global chips
    if hand.value == 21: 
        hand.printPlayerHand()
        hands.append(hand)
        print("Player blackjack!")
        chips += round(hand.bet*(5/2))
    while hand.value < 21:              # play blackjack! only give player options when value below 21
        hand.printPlayerHand()
        time.sleep(1)
        action = input("Hit, stand, double, or split? ").lower()
        # get the correct action for this hand
        if(len(hand.cards)==2):
            if (onlySplitPairs):
                if(hand.cards[0] == hand.cards[1]):
                    correct_action = split_strat[(convertNonAceCard(hand.c[0]),convertNonAceCard(faceUpCard))]
                else:
                    correct_action = strat[(hand.value,hand.soft,convertNonAceCard(faceUpCard))]
            else:
                if convertNonAceCard(hand.cards[0]) == convertNonAceCard(hand.cards[1]):
                    correct_action = split_strat[(convertNonAceCard(hand.cards[0]),convertNonAceCard(faceUpCard))]
                else:
                    correct_action = strat[(hand.value,hand.soft,convertNonAceCard(faceUpCard))]
        else:
            correct_action = strat[(hand.value,hand.soft,convertNonAceCard(faceUpCard))]
            if (correct_action == '\x1b[0;31;40m'+'Double'+'\x1b[0m' and len(hand.cards)>2):
                correct_action = '\x1b[0;33;40m'+'Hit'+'\x1b[0m'

        if action.startswith("h"):
            if(correct_action=='\x1b[0;33;40m'+'Hit'+'\x1b[0m'):
                print("Correct choice!")
            else:
                print(f'Wrong, you should {correct_action}')
            hand.dealCard(deck)
        elif action.startswith("st"):
            if(correct_action=='\x1b[0;32;40m'+'Stand'+'\x1b[0m'):
                print("Correct choice!")
            else:
                print(f"Wrong, you should {correct_action}")
            hands.append(hand)
            break  # leave the loop of betting for this hand
        elif action.startswith("d"): # and ddas is allowed...
            if(correct_action=='\x1b[0;31;40m'+'Double'+'\x1b[0m'):
                print("Correct choice!")
            else:
                print(f"Wrong, you should {correct_action}")
            if ((len(hand.cards) == 2) and (ddas or not hand.split)):  # only allow doubles on two cards
                chips -= hand.bet
                hand.bet += hand.bet
                hand.dealCard(deck)
                if hand.value > 21:
                    hand.printPlayerHand()
                    print(f"Player busts! ({hand.value})")
                if hand.value == 21:
                    hand.printPlayerHand()
                    print("Player blackjack!")
                    chips += round(hand.bet*(5/2))
                    time.sleep(1)
                hands.append(hand)
                break
            else: print("Not a valid move")
        elif action.startswith("sp"): # splits can only happen when a hand has two cards
            if(correct_action=='\x1b[0;34;40m'+'Split'+'\x1b[0m'):
                print("Correct choice!")
            else:
                print(f"Wrong, you should {correct_action}")
            if onlySplitPairs:
                if hand.cards[0] != hand.cards[1]:
                    print("You can't split non-pairs") # at some casinos you can split face cards
                else:
                    playHand(Hand([pHand.cards[0]],hand.bet,True),True,j)
                    chips -= hand.bet
                    playHand(Hand([pHand.cards[1]],hand.bet,True),True,j)
                    break
            else:
                if convertNonAceCard(hand.cards[0]) != convertNonAceCard(hand.cards[1]):
                    print("You can't split cards of different values") # at some casinos you can split face cards
                else:
                    playHand(Hand([pHand.cards[0]],hand.bet,True),True,j)
                    chips -= hand.bet
                    playHand(Hand([pHand.cards[1]],hand.bet,True),True,j)
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
            chips += round(hand.bet*(5/2))
            time.sleep(1)


deck = []
for i in range(decks):
    deck.extend([i for i in range(0,51)])               # will add ability for multi-deck
random.shuffle(deck) # deck should be shuffled and we sequentially remove cards from list using pop


while (chips > 0):
    while True:
        try:
            bet = int(input("Enter your bet: "))
            break
        except ValueError:
            print("Bet must be an integer.")
    if bet < 1:
        print("Bet must be positive.")
        continue
    elif bet > chips:
        print(f"Bet must be less than or equal to the {chips} chips you currently have.")
        continue

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

        for hand in playable_hands:
            hand.printPlayerHand()
            if hand.value > 21: 
                print(f"Player busts! ({hand.value})")
            else:
                if getHandValue(dHand)[0] > 21:
                    print(f"Dealer busts! ({getHandValue(dHand)[0]})")
                    chips += hand.bet*2
                    continue
                if hand.value > getHandValue(dHand)[0]:
                    print(f"Player ({hand.value}) beats dealer ({getHandValue(dHand)[0]})!")
                    chips += hand.bet*2
                elif (hand.value < getHandValue(dHand)[0]) and (getHandValue(dHand)[0] < 22): # dealer can still get BJ here
                    print(f"Dealer ({getHandValue(dHand)[0]}) beats player ({hand.value})!")
                else:
                    print(f"Push! ({getHandValue(dHand)[0]})")
                    chips += hand.bet
    hands = []
    print("Chips: ",chips)
    