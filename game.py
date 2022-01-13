import os
import datetime
import random

cardMap = {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}

def printPlayerHand(hand): # print player's hand cards
    # print("Player hand: ")
    #     for card in hand: print(cardMap[card])
    # print(cardMap[hand])


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
print(deck)
 
chips = 100
# bet = int(input("Enter your bet: "))
bet = 10

p1 = dealCard(deck) # cards represnted as [1,13] but these are not their values
d1 = dealCard(deck) # hidden from players/dealer but dFaceUp is an ace, dealer checks
p2 = dealCard(deck)
d2 = dealCard(deck) # visible to player

printPlayerHand([1,2,3,4])

# create player's hand
pHand=[p1,p2] # list of two integers
dHand=[d1,d2]
# if player gets blackjack they instantly win 1.5 value of their bet
print(f"Dealer card:   {cardMap[d2]}")
# print(f"Player's hand value: {getHandValue(pHand)} ") 
if getHandValue(pHand)==21 and getHandValue(dHand)==21:
    # player pushes
    print("Player cards: ",cardMap[p1]," ",cardMap[p2])
    print(f"Push!")
    # break
elif getHandValue(dHand)==21:
    # dealer blackjack
    print("Player cards: ",cardMap[p1]," ",cardMap[p2])
    print("Dealer blackjack!")
    chips -= bet
    # break
elif getHandValue(pHand)==21:
    # player blackjack
    print("Player cards: ",cardMap[p1]," ",cardMap[p2])
    print("Player blackjack!")
    chips += bet*(3/2)
    # break
else: # player chooses to hit, stand, double down, or split
    while getHandValue(pHand) < 21: # only give player options when value below 21
        print("Player cards: ",cardMap[p1]," ",cardMap[p2])
        action = input("Hit or stand? ").lower()
        if action == "hit":
            print("foo")
            pHand.append(dealCard(deck))
            break