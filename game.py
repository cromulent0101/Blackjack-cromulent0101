import os
import datetime
import random

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
# players place bets
 
startingAmount = 100
# bet = int(input("Enter your bet: "))

# dealer deals first round

p1 = dealCard(deck) # cards represnted as [1,13] but these are not their values
d1 = dealCard(deck) # hidden from players/dealer but dFaceUp is an ace, dealer checks
p2 = dealCard(deck)
d2 = dealCard(deck) # visible to player

# create player's hand
pHand=[p1,p2] # list of two integers
print(p1," ",p2)
print(getHandValue(pHand))
# if player gets blackjack they instantly win 1.5 value of their bet

# if dealer gets blackjack they instantly win

# print(bet)
# print(bet*30)

# player chooses to hit, stand, double down, or split