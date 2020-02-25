#Imports
from usb import write_usb, usb_list_activation
from blutooth import write_blue, blue_list_activation, bluetooth_connect
from help import help
from test import *
from extras import arduino_list_write

#################################
# command_parser
# parameters
#     _input : string  : input from terminal
#      debug : boolean : debug variable
#
# return
#     None
##################################
def command_parser(_input, instructions, debug):
	#split the input into its individual parts
	commands = _input.split()
	
	#loop through all elements in list commands
	for command in commands:
		#set element contained within command to lower
		command = command.lower() 

	#if debug variable is set to true
	if debug:
		#call command_test_print with arguments of first elementof command list and rest of command list
		command_test_print(commands[0], commands[1:])

	#call command recognizer with arguments of first element of command list, rest of command list, and debug variable
	command_recognizer(commands[0], commands[1:], instructions, debug)


##########################################################
# command_recognizer
# parameters
#     command   : single : string  : main command
#     arguments : list   : string  : arguments for command
#     debug     : signle : boolean : debug variable
#
# return
#     None
###########################################################
def command_recognizer(command, arguments, instructions, debug):

	direction = {"forward" : 1, "backward" : 2, "left" : 3, "right" : 4, "stop" : 0}

	####################################################
	# RUN Command ######################################
	####################################################
	if command == "run":
		if len(arguments) == 2 or len(arguments) == 4:
			# 0 = USB  : Single Command
			# 1 = USB  : Program Command List
			# 2 = USB  : Robot Command List
			# 3 = Blue : Single Command
			# 4 = Blue : Program Command List
			# 5 = Blue : Robot Command List

			communication_methods = {"-u" : 0, "-b" : 3}
			command_method = {"-s" : 0, "-d" : 1, "-l" : 2}

			run = {
				0 : write_usb,
				1 : write_usb,
				2 : usb_list_activation,
				3 : write_blue,
				4 : write_blue,
				5 : blue_list_activation
			}

			result = communication_methods[arguments[0]] + command_method[arguments[1]]

			if debug:
				print("Communication Method", str(communication_methods[arguments[0]]))
				print("Command Method", str(command_method[arguments[1]]))
				print("Result", str(result))
				print("Run",run[result])

			if(result == 0 or result == 3):
				run[result](direction.setdefault(arguments[2], 0), arguments[3])
			elif (result == 1 or result == 4):
				run[result](instructions)
			else:
				run[result]()

		else:
			print("No communication method specified")
	#///////////////////////////////////////////////////
	
	####################################################
	# ADD Command ######################################
	####################################################
	elif command == "add":
		if len(arguments) > 0:
			instruction = []

			starts = {"-s" : 0, "-e" : 1, "-i" : 2}

			start = starts.setdefault(arguments[0], 0)

			instruction.append(direction.setdefault(arguments[start], 0))
			instruction.append(int(arguments[start + 1]))

			if start == 2:
				instructions.append(instruction, int(arguments[1]))
			else:
				instructions.append(instruction)
		else:
			print ("This Command takes arguments")
	#///////////////////////////////////////////////////
	
	####################################################
	# LIST Command #####################################
	####################################################
	elif command == "ls":
		index = 0
		while index < len(instructions):
			print ("  " + str(index) + " Direct:" + str(instructions[index][0]) + " Time:" + str(instructions[index][1]))
			index += 1
	#///////////////////////////////////////////////////
	
	####################################################
	# CHANGE Command ###################################
	####################################################
	elif command == "ch":
		if len(arguments) > 0:
			instructions[int(arguments[0])][0] = direction.setdefault(arguments[1], 0)

			instructions[int(arguments[0])][1] = arguments[2]
		else:
			print ("Sorry No arguments specified")
	#///////////////////////////////////////////////////
	
	####################################################
	# REMOVE Command ###################################
	####################################################
	elif command == "rm":
		if len(arguments) > 0:
			if arguments[0] == "-a":
				instructions = instructions[:]
			else:
				instructions = instructions.remove(int(arguments[0]))

		else:
			print ("REQUIRES ARGUMENTS")
	#///////////////////////////////////////////////////
			
	####################################################
	# WRITE Command ####################################
	####################################################
	elif command == "write":
		arduino_list_write(instructions, arguments)
	#///////////////////////////////////////////////////
	
	####################################################
	# Bluetooth Connect Command ########################
	####################################################
	elif command == "blco":
		bluetooth_connect(input("Device Name: "), 1)
	#///////////////////////////////////////////////////
	
	####################################################
	# HELP Command #####################################
	####################################################
	elif command == "help":
		help(arguments)
	#///////////////////////////////////////////////////
	
	####################################################
	# Debug ############################################
	####################################################
	elif command == "debug":
		if debug == False:
			debug = True
		else:
			debug = False
	#///////////////////////////////////////////////////

	####################################################
	# Exit #############################################
	####################################################
	elif command == "exit":
		exit()
	#///////////////////////////////////////////////////

	else:
		print ("Unrecognized Command")


