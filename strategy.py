# strategy from https://www.amazon.com/Basic-Strategy-Card-for-Blackjack/dp/B004XWAWN6

# get the cards from the current Hand
# if they are the same, go to the "split" list
# else, lookup by hand value

aces_strat = {(1,2): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (1,3): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (1,4): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (1,5): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (1,6): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (1,7): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (1,8): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (1,9): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (1,10): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (1,1): '\x1b[0;34;40m'+'Split'+'\x1b[0m'}

twos_strat = {(2,2): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (2,3): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (2,4): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (2,5): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (2,6): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (2,7): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (2,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (2,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (2,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (2,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m'}

threes_strat = {(3,2): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (3,3): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (3,4): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (3,5): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (3,6): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (3,7): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (3,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (3,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (3,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (3,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m'}

fours_strat =  {(4,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (4,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (4,4): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (4,5): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (4,6): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (4,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (4,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (4,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (4,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (4,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m'}

fives_strat =  {(5,2): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
                (5,3): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
                (5,4): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
                (5,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
                (5,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
                (5,7): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
                (5,8): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
                (5,9): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
                (5,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (5,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m'}

sixes_strat  = {(6,2): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (6,3): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (6,4): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (6,5): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (6,6): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (6,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (6,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (6,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (6,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (6,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m'}

sevens_strat = {(7,2): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (7,3): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (7,4): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (7,5): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (7,6): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (7,7): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (7,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (7,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (7,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
                (7,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m'}

eights_strat = {(8,2): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (8,3): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (8,4): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (8,5): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (8,6): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (8,7): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (8,8): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (8,9): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (8,10): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (8,1): '\x1b[0;34;40m'+'Split'+'\x1b[0m'}

nines_strat =  {(9,2): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (9,3): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (9,4): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (9,5): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (9,6): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (9,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (9,8): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (9,9): '\x1b[0;34;40m'+'Split'+'\x1b[0m',
                (9,10): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (9,1): '\x1b[0;32;40m'+'Stand'+'\x1b[0m'}

tens_strat =   {(10,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (10,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (10,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (10,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (10,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (10,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (10,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (10,9): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (10,10): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
                (10,1): '\x1b[0;32;40m'+'Stand'+'\x1b[0m'}

split_strat = {**aces_strat,**twos_strat,**threes_strat,**fours_strat,**fives_strat,**sixes_strat,
                **sevens_strat,**eights_strat,**nines_strat,**tens_strat}

s12_strat = {(12,True,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,True,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,True,4): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,True,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (12,True,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (12,True,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,True,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,True,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,True,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,True,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }


s13_strat = {(13,True,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,True,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,True,4): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,True,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (13,True,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (13,True,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,True,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,True,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,True,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,True,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

s14_strat = {(14,True,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,True,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,True,4): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,True,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (14,True,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (14,True,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,True,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,True,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,True,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,True,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

s15_strat = {(15,True,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,True,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,True,4): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (15,True,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (15,True,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (15,True,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,True,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,True,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,True,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,True,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

s16_strat = {(16,True,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,True,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,True,4): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (16,True,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (16,True,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (16,True,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,True,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,True,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,True,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,True,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

s17_strat = {(17,True,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (17,True,3): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (17,True,4): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (17,True,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (17,True,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (17,True,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (17,True,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (17,True,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (17,True,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (17,True,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

s18_strat = {(17,True,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,True,3): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (17,True,4): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (17,True,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (17,True,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (17,True,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,True,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,True,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (17,True,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (17,True,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }


s18_strat = {(18,True,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,True,3): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (18,True,4): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (18,True,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (18,True,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (18,True,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,True,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,True,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (18,True,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (18,True,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

s19_strat = {(19,True,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,True,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,True,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,True,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,True,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,True,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,True,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,True,9): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,True,10): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,True,1): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            }

s20_strat = {(20,True,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,True,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,True,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,True,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,True,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,True,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,True,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,True,9): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,True,10): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,True,1): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            }

h4_strat = {(4,False,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (4,False,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (4,False,4): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (4,False,5): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (4,False,6): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (4,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (4,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (4,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (4,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (4,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h5_strat = {(5,False,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (5,False,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (5,False,4): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (5,False,5): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (5,False,6): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (5,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (5,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (5,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (5,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (5,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }


h6_strat = {(6,False,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (6,False,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (6,False,4): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (6,False,5): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (6,False,6): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (6,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (6,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (6,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (6,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (6,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h7_strat = {(7,False,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (7,False,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (7,False,4): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (7,False,5): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (7,False,6): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (7,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (7,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (7,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (7,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (7,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h8_strat = {(8,False,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (8,False,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (8,False,4): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (8,False,5): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (8,False,6): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (8,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (8,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (8,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (8,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (8,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h9_strat = {(9,False,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (9,False,3): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (9,False,4): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (9,False,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (9,False,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (9,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (9,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (9,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (9,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (9,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h10_strat = {(10,False,2): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (10,False,3): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (10,False,4): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (10,False,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (10,False,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (10,False,7): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (10,False,8): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (10,False,9): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (10,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (10,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }


h11_strat = {(11,False,2): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (11,False,3): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (11,False,4): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (11,False,5): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (11,False,6): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (11,False,7): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (11,False,8): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (11,False,9): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (11,False,10): '\x1b[0;31;40m'+'Double'+'\x1b[0m',
            (11,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h12_strat = {(12,False,2): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,False,3): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (12,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (12,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (12,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (12,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }


h13_strat = {(13,False,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (13,False,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (13,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (13,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (13,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (13,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (13,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h14_strat = {(14,False,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (14,False,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (14,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (14,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (14,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (14,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (14,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h15_strat = {(15,False,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (15,False,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (15,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (15,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (15,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (15,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (15,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h16_strat = {(16,False,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (16,False,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (16,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (16,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (16,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (16,False,7): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,False,8): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,False,9): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,False,10): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            (16,False,1): '\x1b[0;33;40m'+'Hit'+'\x1b[0m',
            }

h17_strat = {(17,False,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,9): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,10): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,1): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            }

h18_strat = {(17,False,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,9): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,10): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (17,False,1): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            }


h18_strat = {(18,False,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,False,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,False,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,False,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,False,9): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,False,10): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (18,False,1): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            }

h19_strat = {(19,False,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,False,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,False,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,False,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,False,9): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,False,10): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (19,False,1): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            }

h20_strat = {(20,False,2): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,False,3): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,False,4): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,False,5): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,False,6): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,False,7): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,False,8): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,False,9): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,False,10): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            (20,False,1): '\x1b[0;32;40m'+'Stand'+'\x1b[0m',
            }




strat = {**s12_strat,**s13_strat,**s14_strat,**s15_strat,**s16_strat,**s17_strat,**s18_strat,**s19_strat,**s20_strat,
        **h4_strat,**h5_strat,**h6_strat,**h7_strat,**h8_strat,**h9_strat,**h10_strat,
        **h11_strat,**h12_strat,**h13_strat,**h14_strat,**h15_strat,**h16_strat,
        **h17_strat,**h18_strat,**h19_strat,**h20_strat}
    
my_strat = {key: None for key in strat} # populate manually

# print(strat[(14,False,3)])