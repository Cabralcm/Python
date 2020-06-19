# Argparse - Conflict

# Mutual Exclusion
"""
Prevent the user from running an application in both verbose mode vs quiet mode.

use Mutually_Exclusive_group function!

"""

import argparse
def get_args():
    """ """
    parser= argparse.ArgumentParser(
        description = "Arg Parser",
        epilog = "Example Usage"
    )

    #Typically is parser.add_argument()
    #To make mutually exclusive, it is assigned to a variable to store the group object!

    # X and Y are made as mutually exclusive arguments!!! 
    # Can only have X or Y, but not both!!

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-x", "--execute", action="store", help="Help text for option X")
    group.add_argument('-y', help='Help text for option Y', default=False)


    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())

if __name__=="__main__":
    get_args()
