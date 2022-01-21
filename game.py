import random
import time
from cardutils import getHandValue,printDealerHand,convertNonAceCard,cardMap,dealCard

## settings ##
ddas = False
s17 = False
surrender = False
onlySplitPairs = False

deck = ([i for i in range(0,51)]) # will add ability for multi-deck
random.shuffle(deck) # deck should be shuffled and we sequentially remove cards from list using pop

deck = [2,3]  # dealyer's cards
deck.extend([3,3,4,3,5,3,3,3,8,9,10,11,12,13,3,3,4]) # players cards


class Hand:
    def __init__(self,cards:list,bet:int,split:bool):
        self.l = None
        self.r = None
        self.c = cards
        self.b = bet
        self.s = split
        self.value = getHandValue(cards)[0]

    def printPlayerHand(self): # print player's hand cards
        print("Player hand: ",end="  ")
        for card in self.c:
            print(cardMap[card], end ="  ")
        print(f"  ({getHandValue(self.c)[0]})")

    def dealCard(self):
        self.c.append((deck.pop(0) % 13)+1)
        self.value = getHandValue(self.c)[0]


def playHand(hand: Hand, split: bool): # returns winnings (if any) and whether the current hand should be split
    if hand.s: hand.dealCard()          # if this hand is a product of split, deal another card
    global hands
    if hand.value == 21: 
        hand.printPlayerHand()
        hands.append(hand)
        print("Player blackjack!")
    while hand.value < 21:  # play blackjack! only give player options when value below 21
        hand.printPlayerHand()
        action = input("Hit, stand, double, or split? ").lower()
        if action.startswith("h"):
            hand.dealCard()
        elif action.startswith("st"):
            hands.append(hand)
            break  # leave the loop of betting for this hand
        elif action.startswith("d"): # and ddas is allowed...
            if ddas or not split: 
                hand.dealCard()
                hands.append(hand)
                break
            else: print("Not a valid move")
        elif action.startswith("sp"): # splits can only happen when a hand has two cards
            if onlySplitPairs:
                if hand.c[0] != hand.c[1]:
                    print("You can't split non-pairs") # at some casinos you can split face cards
                else:
                    playHand(Hand([pHand.c[0]],hand.b,True),True)
                    playHand(Hand([pHand.c[1]],hand.b,True),True)
                    break
            else:
                if convertNonAceCard(hand.c[0]) != convertNonAceCard(hand.c[1]):
                    print("You can't split cards of different values") # at some casinos you can split face cards
                else:
                    playHand(Hand([pHand.c[0]],hand.b,True),True)
                    playHand(Hand([pHand.c[1]],hand.b,True),True)
                    break
        else:
            print("Not a valid move")
        if hand.value > 21:
            hand.printPlayerHand()
            print(f"Bust ({hand.value})!")
            hands.append(hand)
        if hand.value == 21:
            hand.printPlayerHand()
            hands.append(hand)
            print("Player blackjack!")

chips = 100
# bet = int(input("Enter your bet: "))
bet = 10

# for testing

holeCard = dealCard(deck) # hidden from players/dealer but dFaceUp is an ace, dealer checks
faceUpCard = dealCard(deck) # visible to player

# create player's hand
pHand = Hand([],bet,False)
pHand.dealCard()
pHand.dealCard()

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
    chips -= bet
elif pHand.value==21:    # if player gets blackjack they instantly win 1.5 value of their bet
    # player blackjack
    pHand.printPlayerHand()
    print("Player blackjack!")
    chips += bet*(3/2)
else: 
    playHand(pHand,False)

# for hand in hands:
#     hand.printPlayerHand()

print("Dealer is now dealing...")
while (getHandValue(dHand)[0] < 17): 
    dHand.append(dealCard(deck))
    if getHandValue(dHand)[0] == 17 and getHandValue(dHand)[1] and s17: break
printDealerHand(dHand)


if getHandValue(dHand)[0] > 21:
    print(f"Dealer busts! ({getHandValue(dHand)[0]})")

for hand in hands:
    hand.printPlayerHand()
    if hand.value > getHandValue(dHand)[0]:
        print(f"Player ({hand.value}) beats dealer ({getHandValue(dHand)[0]})!")
    elif hand.value < getHandValue(dHand)[0]:
        print(f"Dealer ({getHandValue(dHand)[0]}) beats player ({hand.value})!")
    else:
        print(f"Push! ({getHandValue(dHand)[0]})")
    