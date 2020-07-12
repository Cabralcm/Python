import argparse
import os

import collections.abc

def main():
    app_defaults = {"username":"admin",
                    "password":"admin"}
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--username')
    parser.add_argument('-p','--password')
    args = parser.parse_args()
    print(args)
    command_line_arguments = {key:value for key,value in vars(args).items()}

    chain = collections.ChainMap(command_line_arguments, os.environ, app_defaults)

    print(chain['username'])

if __name__ == '__main__':
    main()
    os.environ['username'] = 'test'
    main()
