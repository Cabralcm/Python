# Python

import argparse

# parser = argparse.ArgumentParser(
#     description = "A simple argument parser.",
#     epilog="This is where you might put example usage."
# )
# parser.print_help()

####################################################################################################

#usage: _ed_file.py  [-h]

#A simple argument parser

#Optional Arguments:
#   -h, --help  show this help message and exit

#This is where you might put example

def get_args():
    """
    """
    parser = argparse.ArgumentParser(
        description = "A simple argument parser.",
        epilog = "Sample usage."
    )
    return parser.parse_args()

if __name__== '__main__':
    get_args()

