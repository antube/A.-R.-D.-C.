#! /usr/bin/env python3

from commands import Command_Parser

debug = True

while True:
    Full_Command = input("~$ ")
    Full_Command += " "
    Command_Parser(Full_Command, debug)
