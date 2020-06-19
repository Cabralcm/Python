# Python Argparse

import argparse

def get_args():
    """
    """
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    #Required arguments
    parser.add_argument(
        "-x", action="store", required=True, help="Help text for option X")
    #Optional arguments
    parser.add_argument(
        "-y", help="Help text for option Y", default=False)
    parser.add_argument(
        "-z", help="help text for option Z", type=int)
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()

### Short Option

parser.add_argument("-x", action="store", required=True, help="Help text for option X")

## Long Option
## Execute is the long option in this case!
parser.add_argument("-x", "--execute", action="store", required=True, help="Help text for option X")






