import sys
from parse_csv import *

def display_help():
    print("USAGE \n\t./105demography [code]+\n\nDESCRIPTION\n\tcode\tcountry code")


def handle_arguments(args):
    if (len(args) == 2 and args[1] == "-h"):
        display_help()
        return
    if (len(args) < 2):
        print("105demography: Invalid number of arguments, expected a minimum of 1, got 0.")
        exit(84)
    for i in range(1, len(args)):
        if len(args[i]) != 3:
            print("105demography: Invalid argument length, expected 3 but got {}".format(len(args[i])), file=sys.stderr)
            exit(84)
    parse_csv(args)