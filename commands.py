from usb import write_usb, usb_list_activation
from blutooth import bluetooth_connect, write_blue, blue_list_activation
from os.path import exists
from serial import Serial
from help import help
from test import *
from extras import Arduino_List_Write

def Command_Parser(_input, debug):
	commands = _input.split()
	
	for command in commands:
		command = command.lower() 

	if debug:
		Command_Test_Print(commands[0], commands[1:])

	Command_Recognizer(commands[0], commands[1:], debug)

def Command_Recognizer(command, arguments, debug):
	command_direction = []
	command_time = []

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
				run[result](direction.setdefault(arguments[2], "stop"), arguments[3])
			elif (result == 1 or result == 4):
				run[result](command_direction, command_time)
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
			if arguments[0] == "-i":
				#Checks to see what direction the user told the Robot to travel
				command_direction.append(direction.setdefault(arguments[2], "stop"), arguments[1])
				command_time.append(arguments[3])
			elif arguments[0] == "-e":
				#Checks to see what direction the user told the Robot to travel
				command_direction.append(direction.setdefault(arguments[1], "stop"))
				command_time.append(arguments[2])
			else:
				command_direction.append(direction.setdefault(arguments[0], "stop"))
				command_time.append(arguments[1])
		else:
			print ("This Command takes arguments")
	#///////////////////////////////////////////////////
	
	####################################################
	# LIST Command #####################################
	####################################################
	elif command == "ls":
		index = 0
		while index < len(command_direction):
			print ("  " + str(index) + ' Direct:' + str(command_direction[index]) + ' Time:' + str(command_time[index]))
			index += 1
	#///////////////////////////////////////////////////
	
	####################################################
	# CHANGE Command ###################################
	####################################################
	elif command == "ch":
		if len(arguments) > 0:
			command_direction[int(arguments[0])] = direction.setdefault(arguments[1], "stop")

			command_time[int(arguments[0])] = arguments[2]
		else:
			print ("Sorry No arguments specified")
	#///////////////////////////////////////////////////
	
	####################################################
	# REMOVE Command ###################################
	####################################################
	elif command == "rm":
		if len(arguments) > 0 and len(arguments) < 2:
			del(command_direction[int(arguments[0])])
			del(command_time[int(arguments[0])])
		elif len(arguments) > 1:
			if arguments[0] == "-a":
				del(command_direction[:])
				del(command_time[:])
		else:
			print ("Sorry")
	#///////////////////////////////////////////////////
			
	####################################################
	# WRITE Command ####################################
	####################################################
	elif command == "write":
		Arduino_List_Write(command_direction, command_time, arguments)
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
