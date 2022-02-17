# strategy from https://www.amazon.com/Basic-Strategy-Card-for-Blackjack/dp/B004XWAWN6

# get the cards from the current Hand
# if they are the same, go to the "split" list
# else, lookup by hand value

aces_strat = {(1,2): "Split",
                (1,3): "Split",
                (1,4): "Split",
                (1,5): "Split",
                (1,6): "Split",
                (1,7): "Split",
                (1,8): "Split",
                (1,9): "Split",
                (1,10): "Split",
                (1,1): "Split"}

twos_strat = {(2,2): "Split",
                (2,3): "Split",
                (2,4): "Split",
                (2,5): "Split",
                (2,6): "Split",
                (2,7): "Split",
                (2,8): "Hit",
                (2,9): "Hit",
                (2,10): "Hit",
                (2,1): "Hit"}

threes_strat = {(3,2): "Split",
                (3,3): "Split",
                (3,4): "Split",
                (3,5): "Split",
                (3,6): "Split",
                (3,7): "Split",
                (3,8): "Hit",
                (3,9): "Hit",
                (3,10): "Hit",
                (3,1): "Hit"}

fours_strat =  {(4,2): "Hit",
                (4,3): "Hit",
                (4,4): "Hit",
                (4,5): "Split",
                (4,6): "Split",
                (4,7): "Hit",
                (4,8): "Hit",
                (4,9): "Hit",
                (4,10): "Hit",
                (4,1): "Hit"}

fives_strat =  {(5,2): "Double",
                (5,3): "Double",
                (5,4): "Double",
                (5,5): "Double",
                (5,6): "Double",
                (5,7): "Double",
                (5,8): "Double",
                (5,9): "Double",
                (5,10): "Hit",
                (5,1): "Hit"}

sixes_strat  = {(6,2): "Split",
                (6,3): "Split",
                (6,4): "Split",
                (6,5): "Split",
                (6,6): "Split",
                (6,7): "Hit",
                (6,8): "Hit",
                (6,9): "Hit",
                (6,10): "Hit",
                (6,1): "Hit"}

sevens_strat = {(7,2): "Split",
                (7,3): "Split",
                (7,4): "Split",
                (7,5): "Split",
                (7,6): "Split",
                (7,7): "Split",
                (7,8): "Hit",
                (7,9): "Hit",
                (7,10): "Hit",
                (7,1): "Hit"}

eights_strat = {(8,2): "Split",
                (8,3): "Split",
                (8,4): "Split",
                (8,5): "Split",
                (8,6): "Split",
                (8,7): "Split",
                (8,8): "Split",
                (8,9): "Split",
                (8,10): "Split",
                (8,1): "Split"}

nines_strat =  {(9,2): "Split",
                (9,3): "Split",
                (9,4): "Split",
                (9,5): "Split",
                (9,6): "Split",
                (9,7): "Stand",
                (9,8): "Split",
                (9,9): "Split",
                (9,10): "Stand",
                (9,1): "Stand"}

tens_strat =   {(10,2): "Stand",
                (10,3): "Stand",
                (10,4): "Stand",
                (10,5): "Stand",
                (10,6): "Stand",
                (10,7): "Stand",
                (10,8): "Stand",
                (10,9): "Stand",
                (10,10): "Stand",
                (10,1): "Stand"}

split_strat = {**aces_strat,**twos_strat,**threes_strat,**fours_strat,**fives_strat,**sixes_strat,
                **sevens_strat,**eights_strat,**nines_strat,**tens_strat}



strat = {}