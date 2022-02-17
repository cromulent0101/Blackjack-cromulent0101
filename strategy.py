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

s12_strat = {(12,True,2): "Hit",
            (12,True,3): "Hit",
            (12,True,4): "Hit",
            (12,True,5): "Double",
            (12,True,6): "Double",
            (12,True,7): "Hit",
            (12,True,8): "Hit",
            (12,True,9): "Hit",
            (12,True,10): "Hit",
            (12,True,1): "Hit",
            }


s13_strat = {(13,True,2): "Hit",
            (13,True,3): "Hit",
            (13,True,4): "Hit",
            (13,True,5): "Double",
            (13,True,6): "Double",
            (13,True,7): "Hit",
            (13,True,8): "Hit",
            (13,True,9): "Hit",
            (13,True,10): "Hit",
            (13,True,1): "Hit",
            }

s14_strat = {(14,True,2): "Hit",
            (14,True,3): "Hit",
            (14,True,4): "Hit",
            (14,True,5): "Double",
            (14,True,6): "Double",
            (14,True,7): "Hit",
            (14,True,8): "Hit",
            (14,True,9): "Hit",
            (14,True,10): "Hit",
            (14,True,1): "Hit",
            }

s15_strat = {(15,True,2): "Hit",
            (15,True,3): "Hit",
            (15,True,4): "Double",
            (15,True,5): "Double",
            (15,True,6): "Double",
            (15,True,7): "Hit",
            (15,True,8): "Hit",
            (15,True,9): "Hit",
            (15,True,10): "Hit",
            (15,True,1): "Hit",
            }

s16_strat = {(16,True,2): "Hit",
            (16,True,3): "Hit",
            (16,True,4): "Double",
            (16,True,5): "Double",
            (16,True,6): "Double",
            (16,True,7): "Hit",
            (16,True,8): "Hit",
            (16,True,9): "Hit",
            (16,True,10): "Hit",
            (16,True,1): "Hit",
            }

s17_strat = {(17,True,2): "Hit",
            (17,True,3): "Double",
            (17,True,4): "Double",
            (17,True,5): "Double",
            (17,True,6): "Double",
            (17,True,7): "Hit",
            (17,True,8): "Hit",
            (17,True,9): "Hit",
            (17,True,10): "Hit",
            (17,True,1): "Hit",
            }

s18_strat = {(17,True,2): "Stand",
            (17,True,3): "Double",
            (17,True,4): "Double",
            (17,True,5): "Double",
            (17,True,6): "Double",
            (17,True,7): "Stand",
            (17,True,8): "Stand",
            (17,True,9): "Hit",
            (17,True,10): "Hit",
            (17,True,1): "Hit",
            }


s18_strat = {(18,True,2): "Stand",
            (18,True,3): "Double",
            (18,True,4): "Double",
            (18,True,5): "Double",
            (18,True,6): "Double",
            (18,True,7): "Stand",
            (18,True,8): "Stand",
            (18,True,9): "Hit",
            (18,True,10): "Hit",
            (18,True,1): "Hit",
            }

s19_strat = {(19,True,2): "Stand",
            (19,True,3): "Stand",
            (19,True,4): "Stand",
            (19,True,5): "Stand",
            (19,True,6): "Stand",
            (19,True,7): "Stand",
            (19,True,8): "Stand",
            (19,True,9): "Stand",
            (19,True,10): "Stand",
            (19,True,1): "Stand",
            }

s20_strat = {(20,True,2): "Stand",
            (20,True,3): "Stand",
            (20,True,4): "Stand",
            (20,True,5): "Stand",
            (20,True,6): "Stand",
            (20,True,7): "Stand",
            (20,True,8): "Stand",
            (20,True,9): "Stand",
            (20,True,10): "Stand",
            (20,True,1): "Stand",
            }

h5_strat = {(5,False,2): "Hit",
            (5,False,3): "Hit",
            (5,False,4): "Hit",
            (5,False,5): "Hit",
            (5,False,6): "Hit",
            (5,False,7): "Hit",
            (5,False,8): "Hit",
            (5,False,9): "Hit",
            (5,False,10): "Hit",
            (5,False,1): "Hit",
            }


h6_strat = {(6,False,2): "Hit",
            (6,False,3): "Hit",
            (6,False,4): "Hit",
            (6,False,5): "Hit",
            (6,False,6): "Hit",
            (6,False,7): "Hit",
            (6,False,8): "Hit",
            (6,False,9): "Hit",
            (6,False,10): "Hit",
            (6,False,1): "Hit",
            }

h7_strat = {(7,False,2): "Hit",
            (7,False,3): "Hit",
            (7,False,4): "Hit",
            (7,False,5): "Hit",
            (7,False,6): "Hit",
            (7,False,7): "Hit",
            (7,False,8): "Hit",
            (7,False,9): "Hit",
            (7,False,10): "Hit",
            (7,False,1): "Hit",
            }

h8_strat = {(8,False,2): "Hit",
            (8,False,3): "Hit",
            (8,False,4): "Hit",
            (8,False,5): "Hit",
            (8,False,6): "Hit",
            (8,False,7): "Hit",
            (8,False,8): "Hit",
            (8,False,9): "Hit",
            (8,False,10): "Hit",
            (8,False,1): "Hit",
            }

h9_strat = {(9,False,2): "Hit",
            (9,False,3): "Double",
            (9,False,4): "Double",
            (9,False,5): "Double",
            (9,False,6): "Double",
            (9,False,7): "Hit",
            (9,False,8): "Hit",
            (9,False,9): "Hit",
            (9,False,10): "Hit",
            (9,False,1): "Hit",
            }

h10_strat = {(10,False,2): "Double",
            (10,False,3): "Double",
            (10,False,4): "Double",
            (10,False,5): "Double",
            (10,False,6): "Double",
            (10,False,7): "Double",
            (10,False,8): "Double",
            (10,False,9): "Double",
            (10,False,10): "Hit",
            (10,False,1): "Hit",
            }


h11_strat = {(11,False,2): "Double",
            (11,False,3): "Double",
            (11,False,4): "Double",
            (11,False,5): "Double",
            (11,False,6): "Double",
            (11,False,7): "Double",
            (11,False,8): "Double",
            (11,False,9): "Double",
            (11,False,10): "Double",
            (11,False,1): "Hit",
            }

h12_strat = {(12,False,2): "Hit",
            (12,False,3): "Hit",
            (12,False,4): "Stand",
            (12,False,5): "Stand",
            (12,False,6): "Stand",
            (12,False,7): "Hit",
            (12,False,8): "Hit",
            (12,False,9): "Hit",
            (12,False,10): "Hit",
            (12,False,1): "Hit",
            }


h13_strat = {(13,False,2): "Stand",
            (13,False,3): "Stand",
            (13,False,4): "Stand",
            (13,False,5): "Stand",
            (13,False,6): "Stand",
            (13,False,7): "Hit",
            (13,False,8): "Hit",
            (13,False,9): "Hit",
            (13,False,10): "Hit",
            (13,False,1): "Hit",
            }

h14_strat = {(14,False,2): "Stand",
            (14,False,3): "Stand",
            (14,False,4): "Stand",
            (14,False,5): "Stand",
            (14,False,6): "Stand",
            (14,False,7): "Hit",
            (14,False,8): "Hit",
            (14,False,9): "Hit",
            (14,False,10): "Hit",
            (14,False,1): "Hit",
            }

h15_strat = {(15,False,2): "Stand",
            (15,False,3): "Stand",
            (15,False,4): "Stand",
            (15,False,5): "Stand",
            (15,False,6): "Stand",
            (15,False,7): "Hit",
            (15,False,8): "Hit",
            (15,False,9): "Hit",
            (15,False,10): "Hit",
            (15,False,1): "Hit",
            }

h16_strat = {(16,False,2): "Stand",
            (16,False,3): "Stand",
            (16,False,4): "Stand",
            (16,False,5): "Stand",
            (16,False,6): "Stand",
            (16,False,7): "Hit",
            (16,False,8): "Hit",
            (16,False,9): "Hit",
            (16,False,10): "Hit",
            (16,False,1): "Hit",
            }

h17_strat = {(17,False,2): "Stand",
            (17,False,3): "Stand",
            (17,False,4): "Stand",
            (17,False,5): "Stand",
            (17,False,6): "Stand",
            (17,False,7): "Stand",
            (17,False,8): "Stand",
            (17,False,9): "Stand",
            (17,False,10): "Stand",
            (17,False,1): "Stand",
            }

h18_strat = {(17,False,2): "Stand",
            (17,False,3): "Stand",
            (17,False,4): "Stand",
            (17,False,5): "Stand",
            (17,False,6): "Stand",
            (17,False,7): "Stand",
            (17,False,8): "Stand",
            (17,False,9): "Stand",
            (17,False,10): "Stand",
            (17,False,1): "Stand",
            }


h18_strat = {(18,False,2): "Stand",
            (18,False,3): "Stand",
            (18,False,4): "Stand",
            (18,False,5): "Stand",
            (18,False,6): "Stand",
            (18,False,7): "Stand",
            (18,False,8): "Stand",
            (18,False,9): "Stand",
            (18,False,10): "Stand",
            (18,False,1): "Stand",
            }

h19_strat = {(19,False,2): "Stand",
            (19,False,3): "Stand",
            (19,False,4): "Stand",
            (19,False,5): "Stand",
            (19,False,6): "Stand",
            (19,False,7): "Stand",
            (19,False,8): "Stand",
            (19,False,9): "Stand",
            (19,False,10): "Stand",
            (19,False,1): "Stand",
            }

h20_strat = {(20,False,2): "Stand",
            (20,False,3): "Stand",
            (20,False,4): "Stand",
            (20,False,5): "Stand",
            (20,False,6): "Stand",
            (20,False,7): "Stand",
            (20,False,8): "Stand",
            (20,False,9): "Stand",
            (20,False,10): "Stand",
            (20,False,1): "Stand",
            }



strat = {**s12_strat,**s13_strat,**s14_strat,**s15_strat,**s16_strat,**s17_strat,**s18_strat,**s19_strat,**s20_strat,
        **h5_strat,**h6_strat,**h7_strat,**h8_strat,**h9_strat,**h10_strat,
        **h11_strat,**h12_strat,**h13_strat,**h14_strat,**h15_strat,**h16_strat,
        **h17_strat,**h18_strat,**h19_strat,**h20_strat}
        
# print(strat[(14,False,3)])