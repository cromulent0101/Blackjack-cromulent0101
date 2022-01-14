import random

cardMap = {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}

def printPlayerHand(hand): # print player's hand cards
    print("Player hand: ",end="  ")
    for card in hand:
        print(cardMap[card], end ="  ")
    print("")

def printDealerHand(hand): # print player's hand cards
    print("Dealer hand: ",end="  ")
    for card in hand:
        print(cardMap[card], end ="  ")
    print("")

def convertNonAceCard(card): # card will be [2,13]
    if card > 10:
        return 10
    else:
        return card 

def getHandValue(hand): # easiest to determine value of cards in hand context because of aces
    total = 0
    for card in hand: # hand should be a set instead of list since order does not matter
        if card > 1: # NOT an ace
            total += convertNonAceCard(card)
        else:       # is an ace
            if total > 10:
                total += 1
            else:
                total += 11
    return total

def checkBlackjack():
    pass

def dealCard(deck):
    return (deck.pop() % 13)+1

deck = ([i for i in range(0,51)]) 
random.shuffle(deck) # deck should be shuffled and we sequentially remove cards from list using pop
# print(deck)
 
chips = 100
# bet = int(input("Enter your bet: "))
bet = 10

p1 = dealCard(deck) # cards represnted as [1,13] but these are not their values
holeCard = dealCard(deck) # hidden from players/dealer but dFaceUp is an ace, dealer checks
p2 = dealCard(deck)
faceUpCard = dealCard(deck) # visible to player

# create player's hand
pHand=[p1,p2] # list of two integers
dHand=[holeCard,faceUpCard]
print(f"Dealer card:   {cardMap[faceUpCard]}")

if getHandValue(pHand)==21 and getHandValue(dHand)==21:
    # player pushes
    printPlayerHand(pHand)
    print(f"Push!")
elif getHandValue(dHand)==21:
    # dealer blackjack
    printDealerHand(pHand)
    print("Dealer blackjack!")
    chips -= bet
elif getHandValue(pHand)==21: # if player gets blackjack they instantly win 1.5 value of their bet
    # player blackjack
    printPlayerHand(pHand)
    print("Player blackjack!")
    chips += bet*(3/2)

else: # player chooses to hit, stand, double down, or split
    while getHandValue(pHand) < 21: # only give player options when value below 21
        printPlayerHand(pHand)
        action = input("Hit or stand? ").lower()
        if action == "hit":
            pHand.append(dealCard(deck))
        elif action == "stand":
            break  # leave the loop of betting and dealer does their thing
        else:
            print("Not a valid move")
        
if getHandValue(pHand) > 21:
    printPlayerHand(pHand)
    print(f"Bust ({getHandValue(pHand)})!")
else: # Now the dealer deals
    print("Dealer is now dealing...")
    while getHandValue(dHand) < 17: # S17 for now. dealer stands on soft 17
        dHand.append(dealCard(deck))
    printDealerHand(dHand)
    printPlayerHand(pHand)
    if getHandValue(dHand) > 21:
        print(f"Dealer busts! ({getHandValue(dHand)})")
    elif getHandValue(pHand) > getHandValue(dHand):
        print(f"Player ({getHandValue(pHand)}) beats dealer ({getHandValue(dHand)})!")
    elif getHandValue(pHand) < getHandValue(dHand):
        print(f"Dealer ({getHandValue(dHand)}) beats player ({getHandValue(pHand)})!")
    else:
        print(f"Push! ({getHandValue(dHand)})")
    