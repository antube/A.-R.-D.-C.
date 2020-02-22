from usb import Write_USB
from blutooth import Write_Blue, Bluetooth_connect
from os.path import exists
from serial import Serial
from help import help
from test import *
from extras import Arduino_List_Write

def Command_Parser(_input, debug):
	CMD = ""
	Arguments = []
	ON_CMD = True
	argument = ""
    
	for i in _input:
		if ON_CMD and i == " ":
			ON_CMD = False
		elif ON_CMD:
			CMD += i
		elif not ON_CMD and i == " ":
			Arguments.append(argument)
			argument = ""
		elif not ON_CMD:
			argument += i
	
	if debug:
		Command_Test_Print(CMD, Arguments)

	Command_Recognizer(CMD, Arguments, debug)

def Command_Recognizer(CMD, Arguments, debug):
	command_direction = []
	command_time = []

	####################################################
	# RUN Command ######################################
	####################################################
	if CMD.lower() == "run":
		if len(Arguments) > 0:
			if Arguments[0].lower() == "/u":
				Write_USB(command_direction, command_time)
			elif Arguments[0].lower() == "/b":
				Write_Blue(command_direction, command_time)
			elif Arguments[0].lower() == "ls":
				if exists('/dev/ttyACM0'):
					serUSB = Serial('/dev/ttyACM0')
					serUSB.baudrate = 9600
					#serial_read = serUSB.readline()
					data = 'icommand,5;'
					serUSB.write(data.encode())
				elif exists('/dev/tty.usbserial'):
					serUSB = Serial('/dev/tty.usbserial')
					serUSB.baudrate = 9600
					#serial_read = serUSB.readline()
					data = 'icommand,5;'
					serUSB.write(data.encode())
			else:
				if exists('/dev/ttyACM0'):
					serUSB = Serial('/dev/ttyACM0')
					serUSB.baudrate = 9600
					#serial_read = serUSB.readline()
					if Arguments[0].lower() == "/l":
						data = 'icommand,' + str(5) + ';'
					else:
						data = 'icommand,' + Arguments[0] + ',' + Arguments[1] +';'
						serUSB.write(data.encode())

					print ("Running")
				elif exists('/dev/tty.usbserial'):
					serUSB = Serial('/dev/tty.usbserial')
					serUSB.baudrate = 9600
					if Arguments[0].lower() == "/l":
						data = 'icommand,' + str(5) + ';'
					else:
						data = 'icommand,' + Arguments[0] + ',' + Arguments[1] +';'
						serUSB.write(data.encode())

					print ("Running")
				else:
					print ("Sorry No Arduino Connected")
		else:
			print ("Beginning Run")
			Write_USB(command_direction, command_time)
			print ("Done Run")
	#///////////////////////////////////////////////////
	
	####################################################
	# ADD Command ######################################
	####################################################
	elif CMD.lower() == "add":
		if len(Arguments) > 0:
			if Arguments[0].lower() == "/i":
				#Checks to see what direction the user told the Robot to travel
				if Arguments[2].lower() == "forward":
					command_direction.append(1, Arguments[1])
				elif Arguments[2].lower() == "backward":
					command_direction.append(2, Arguments[1])
				elif Arguments[2].lower() == "left":
					command_direction.append(3, Arguments[1])
				elif Arguments[2].lower() == "right":
					command_direction.append(4, Arguments[1])
				else:
					command_direction.append(0, Arguments[1])
				command_time.append(Arguments[3])
			elif Arguments[0].lower() == "/e":
				#Checks to see what direction the user told the Robot to travel
				if Arguments[1].lower() == "forward":
					command_direction.append(1)
				elif Arguments[1].lower() == "backward":
					command_direction.append(2)
				elif Arguments[1].lower() == "left":
					command_direction.append(3)
				elif Arguments[1].lower() == "right":
					command_direction.append(4)
				else:
					command_direction.append(0)

				command_time.append(Arguments[1])
			else:
				if Arguments[0].lower() == "forward":
					command_direction.append(1)
				elif Arguments[0].lower() == "backward":
					command_direction.append(2)
				elif Arguments[0].lower() == "left":
					command_direction.append(3)
				elif Arguments[0].lower() == "right":
					command_direction.append(4)
				else:
					command_direction.append(0)

				command_time.append(Arguments[1])
		else:
			print ("This Command takes Arguments")
	#///////////////////////////////////////////////////
	
	####################################################
	# LIST Command #####################################
	####################################################
	elif CMD.lower() == "ls":
		index = 0
		while index < len(command_direction):
			print ("  "+str(index)+' Direct:'+str(command_direction[index])+' Time:'+str(command_time[index]))
			index += 1
	#///////////////////////////////////////////////////
	
	####################################################
	# CHANGE Command ###################################
	####################################################
	elif CMD.lower() == "ch":
		if len(Arguments) > 0:
			if Arguments[1].lower() == "forward":
				command_direction[int(Arguments[0])] = 1
			elif Arguments[1].lower() == "backward":
				command_direction[int(Arguments[0])] = 2
			elif Arguments[1].lower() == "left":
				command_direction[int(Arguments[0])] = 3
			elif Arguments[1].lower() == "right":
				command_direction[int(Arguments[0])] = 4
			else:
				command_direction[int(Arguments[0])] = 0
			command_time[int(Arguments[0])] = Arguments[2]
		else:
			print ("Sorry")
	#///////////////////////////////////////////////////
	
	####################################################
	# REMOVE Command ###################################
	####################################################
	elif CMD.lower() == "rm":
		if len(Arguments) > 0 and len(Arguments) < 2:
			del(command_direction[int(Arguments[0])])
			del(command_time[int(Arguments[0])])
		elif len(Arguments) > 1:
			if Arguments[0] == "/a":
				del(command_direction[:])
				del(command_time[:])
		else:
			print ("Sorry")
	#///////////////////////////////////////////////////
			
	####################################################
	# WRITE Command ####################################
	####################################################
	elif CMD.lower() == "write":
		Arduino_List_Write(command_direction, command_time, Arguments)
	#///////////////////////////////////////////////////
	
	####################################################
	# Bluetooth Connect Command ########################
	####################################################
	elif CMD.lower() == "blco":
		Bluetooth_connect(input("Device Name: "), 1)
	#///////////////////////////////////////////////////
	
	####################################################
	# HELP Command #####################################
	####################################################
	elif CMD.lower() == "help":
		help(Arguments)
	#///////////////////////////////////////////////////
	
	####################################################
	# Debug ############################################
	####################################################
	elif CMD.lower() == "debug":
		if debug == False:
			debug = True
		else:
			debug = False
	#///////////////////////////////////////////////////
	else:
		print ("Unrecognized Command")
