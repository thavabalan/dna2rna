#!/usr/bin/python3
def D_2_R(str):
    before = 'T'
    after = 'U'
    trans_table = str.maketrans(before,after)
    return (str.translate(trans_table))


LOGO = r'''
        ___  _  _____   ___  __  ______  _  _____
      / _ \/ |/ / _ | |_  |/  |/  / _ \/ |/ / _ |
     / // /    / __ |/ __// /|_/ / , _/    / __ |
    /____/_/|_/_/ |_/____/_/  /_/_/|_/_/|_/_/ |_|

            Welcome to MagneChio n2x
                Version 1.0
  You can get mRNA Sequence by entering 24 bp DNA Sequence
'''
END = r'''
  Thank you for using MagneChio n2x v1.0
  All rights reserved.Spectrum Institute of Science & Technology.Copyright 2019
'''

print (LOGO)
DNA = input('Enter Sequence bp1:')

print('Your DNA Sequence: ' + DNA)
print ('Resultant mRNA Sequence is: ' + D_2_R(DNA))

restart = input('Press Y to run another test and E to exit.').lower()
if restart == "y":
    D_2_R()
if restart == "e":
    exit()
else:
    print(END)
