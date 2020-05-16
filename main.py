#! /usr/bin/env python3

"""
" Name : main.py
" Author : Andrew Brown
" Date : May 16 2020
" Description :
"
"""

#import command_parser from commands file
from commands import command_parser

def main():
    """
    " Name : main
    "
    " Description :
    "
    "
    " Parameters :
    "       None
    "
    " Return :
    "       None
    """
    instructions = []

    #Create 1 infinite loop
    while True:
        #Call command_parser and pass in input from terminal and set debug to True
        command_parser(input("~$"), instructions, False)

if __name__ == "__main__":
    main()
