#! /usr/bin/env python3

#import command_parser from commands file
from commands import command_parser

instructions = []

#Create 1 infinite loop
while True:
    #Call command_parser and pass in input from terminal and set debug to True
    command_parser(input("~$"), instructions, False)
