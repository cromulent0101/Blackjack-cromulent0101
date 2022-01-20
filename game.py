import random

## settings ##
ddas = False
s17 = False
surrender = False
decks = 3

cardMap = {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}

def printPlayerHand(hand): # print player's hand cards
    print("Player hand: ",end="  ")
    for card in hand:
        print(cardMap[card], end ="  ")
    print("")

def printDealerHand(hand): # print dealer's hand cards
    print("Dealer hand: ",end="  ")
    for card in hand:
        print(cardMap[card], end ="  ")
    print("")

def convertNonAceCard(card): # card will be [2,13]
    if card > 10:
        return 10
    else:
        return card 

def getHandValue(hand):                         # easiest to determine value of cards in hand context because of aces
    hardTotal = 0
    aceCount = 0
    # run through hard hards first and keep a total, then run thru aces
    for card in hand:                           # hand should be a set instead of list since order does not matter
        if card > 1:                            # NOT an ace
            hardTotal += convertNonAceCard(card)
    else:                                       # is an ace
            aceCount += 1
    if hardTotal >= 11:                         # can't be soft 17
        return hardTotal + aceCount, False
    elif aceCount > 0:                          # could be soft 17
        if (hardTotal + 10 + aceCount) > 21: return (hardTotal + aceCount), False
        else: return (hardTotal + 10 + aceCount), (17==(hardTotal + 10 + aceCount)) 
    else:                                       # can't be soft 17
        return hardTotal, False

def dealCard(deck):
    return (deck.pop() % 13)+1

deck = []
for i in range(decks):
    deck.extend([i for i in range(0,51)])               # will add ability for multi-deck
random.shuffle(deck) # deck should be shuffled and we sequentially remove cards from list using pop
print(deck, deck.count(31))
chips = 100
# bet = int(input("Enter your bet: "))
bet = 10

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
elif getHandValue(pHand)[0]==21: # if player gets blackjack they instantly win 1.5 value of their bet
    # player blackjack
    printPlayerHand(pHand)
    print("Player blackjack!")
    chips += bet*(3/2)
else: # player chooses to hit, stand, double down, or split
    while getHandValue(pHand)[0] < 21: # only give player options when value below 21
        printPlayerHand(pHand)
        action = input("Hit, stand, or double? ").lower()
        if action.startswith("h"):
            pHand.append(dealCard(deck))
        elif action.startswith("s"):
            break  # leave the loop of betting and dealer does their thing
        elif action.startswith("d"):
            pHand.append(dealCard(deck))
            bet += bet
            break
        else:
            print("Not a valid move")
    if getHandValue(pHand)[0] > 21:
        printPlayerHand(pHand)
        print(f"Bust ({getHandValue(pHand)[0]})!")
    else: # Now the dealer deals
        print("Dealer is now dealing...")
        while (getHandValue(dHand)[0] < 17): 
            dHand.append(dealCard(deck))
            if getHandValue(dHand)[0] == 17 and getHandValue(dHand)[1] and s17: break
        printDealerHand(dHand)
        printPlayerHand(pHand)
        if getHandValue(dHand)[0] > 21:
            print(f"Dealer busts! ({getHandValue(dHand)[0]})")
        elif getHandValue(pHand)[0] > getHandValue(dHand)[0]:
            print(f"Player ({getHandValue(pHand)[0]}) beats dealer ({getHandValue(dHand)[0]})!")
        elif getHandValue(pHand)[0] < getHandValue(dHand)[0]:
            print(f"Dealer ({getHandValue(dHand)[0]}) beats player ({getHandValue(pHand)[0]})!")
        else:
            print(f"Push! ({getHandValue(dHand)[0]})")
    