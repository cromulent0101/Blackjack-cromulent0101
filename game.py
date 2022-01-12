import os
import datetime
import random

# def convertToCardValue(int card):
    # checks if a card is a face card (value 10), or if ace

def getHandValue(hand):
    total = 0
    for card in hand:
        if 11 < card < 1: # regular card
            total += card
            break
        if card > 10: # face card
            total += 10 
    return total


def checkBlackjack():
    pass

deck = ([i for i in range(0,51)]) 
random.shuffle(deck) # deck should be shuffled and we sequentially remove cards from list using pop
print(deck)
# players place bets
 
startingAmount = 100
bet = int(input("Enter your bet: "))

# dealer deals first round

dFaceDown = deck.pop # hidden from players/dealer but dFaceUp is an ace, dealer checks
# we will need to convert face cards into their true value once added to hand
## but what about spliting?
# aces may be con
p1 = (deck.pop() % 13)+1 # cards represnted as [1,13] but these are not their values
print(p1)
p2 = (deck.pop() % 13)+1

# create player's hand
pHand=[p1,p2] # list of two integers
print(p1," ",p2)
# if player gets blackjack they instantly win 1.5 value of their bet
if pHand.count(1) and (pHand.count(10) or pHand.count(11) or pHand.count(12) or pHand.count(13)))

# if dealer gets blackjack they instantly win

print(bet)
print(bet*30)

# player chooses to hit, stand, double down, or split