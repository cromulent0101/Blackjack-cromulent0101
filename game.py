import random
import time
from cardutils import getHandValue,printDealerHand,convertNonAceCard,cardMap

## settings ##
ddas = False
s17 = False
surrender = False


class Hand:
    def __init__(self,cards:list,bet:int,split:bool):
        self.l = None
        self.r = None
        self.c = cards
        self.b = bet
        self.s = split
        self.value = getHandValue(cards)

    def printPlayerHand(self): # print player's hand cards
        print("Player hand: ",end="  ")
        for card in self.c:
            print(cardMap[card], end ="  ")
        print("")

    def dealCard(self):
        self.c.append(deck.pop() % 13)+1
        self.value = getHandValue(self.c)

def playHand(hand: Hand, split: bool): # returns winnings (if any) and whether the current hand should be split
    while hand.value < 21:  # play blackjack! only give player options when value below 21
        hand.printPlayerHand()
        action = input("Hit, stand, double, or split? ").lower()
        if action.startswith("h"):
            hand.dealCard()
        elif action.startswith("st"):
            break  # leave the loop of betting for this hand
        elif action.startswith("d") and ddas: # and ddas is allowed...
            hand.dealCard()
            playableHands.pop()
            break
        elif action.startswith("sp"): # splits can only happen when a hand has two cards
            if hand[0] != hand[1]:
                print("You can't split non-pairs") # at some casinos you can split face cards
            else:
                pass
        else:
            print("Not a valid move")
        if getHandValue(hand)[0] > 21:
            hand.printPlayerHand()
            print(f"Bust ({getHandValue(hand)[0]})!")


deck = ([i for i in range(0,51)]) # will add ability for multi-deck
random.shuffle(deck) # deck should be shuffled and we sequentially remove cards from list using pop
 
chips = 100
# bet = int(input("Enter your bet: "))
bet = 10

pHand = Hand([],bet,False)
dHand = Hand([],0,False)
p1 = dealCard(deck) # cards represnted as [1,13] but these are not their values
holeCard = dealCard(deck) # hidden from players/dealer but dFaceUp is an ace, dealer checks
p2 = dealCard(deck)
faceUpCard = dealCard(deck) # visible to player

# create player's hand
pHand=[p1,p2] # list of two integers
dHand=[faceUpCard,holeCard]
print(f"Dealer card:   {cardMap[faceUpCard]}")

if getHandValue(pHand)[0]==21 and getHandValue(dHand)[0]==21: # blackjack push
    printPlayerHand(pHand)
    print(f"Push!")
elif getHandValue(dHand)[0]==21:     # dealer blackjack
    printDealerHand(pHand)
    print("Dealer blackjack!")
    chips -= bet
elif getHandValue(pHand)[0]==21:    # if player gets blackjack they instantly win 1.5 value of their bet
    # player blackjack
    printPlayerHand(pHand)
    print("Player blackjack!")
    chips += bet*(3/2)
else: 
    playableHands = [pHand]
    totalHands = [pHand]
    while(playableHands):                   # while there is a playable hand
        time.sleep(0.1)
        pHand = playableHands[0]            # current hand is first/last playable hand (need to see whch)
        while getHandValue(pHand)[0] < 21:  # play blackjack! only give player options when value below 21
            printPlayerHand(pHand)
            action = input("Hit, stand, double, or split? ").lower()
            if action.startswith("h"):
                pHand.append(dealCard(deck))
            elif action.startswith("st"):
                playableHands.pop()
                break  # leave the loop of betting for this hand
            elif action.startswith("d"): # and ddas is allowed...
                pHand.append(dealCard(deck))
                bet += bet
                playableHands.pop()
                break
            elif action.startswith("sp"): # splits can only happen when a hand has two cards
                if pHand[0] != pHand[1]:
                    print("You can't split non-pairs") # at some casinos you can split face cards
                else:
                    totalHands.pop()
                    playableHands.pop()
                    splitCard1 = dealCard(deck)     # this is NOT how cards are dealt after a split
                    splitCard2 = dealCard(deck)
                    totalHands.append([pHand[0],splitCard1])
                    playableHands.append([pHand[0],splitCard1])
                    totalHands.append([pHand[1],splitCard2])
                    playableHands.append([pHand[1],splitCard2])
            else:
                print("Not a valid move")
        if getHandValue(pHand)[0] > 21:
            printPlayerHand(pHand)
            print(f"Bust ({getHandValue(pHand)[0]})!")


    # else: # Now the dealer deals after all hands are bust/stood
    #     print("Dealer is now dealing...")
    #     while (getHandValue(dHand)[0] < 17): 
    #         dHand.append(dealCard(deck))
    #         if getHandValue(dHand)[0] == 17 and getHandValue(dHand)[1] and s17: break
    #     printDealerHand(dHand)
    #     printPlayerHand(pHand)


    #     if getHandValue(dHand)[0] > 21:
    #         print(f"Dealer busts! ({getHandValue(dHand)[0]})")
    #     elif getHandValue(pHand)[0] > getHandValue(dHand)[0]:
    #         print(f"Player ({getHandValue(pHand)[0]}) beats dealer ({getHandValue(dHand)[0]})!")
    #     elif getHandValue(pHand)[0] < getHandValue(dHand)[0]:
    #         print(f"Dealer ({getHandValue(dHand)[0]}) beats player ({getHandValue(pHand)[0]})!")
    #     else:
    #         print(f"Push! ({getHandValue(dHand)[0]})")
    