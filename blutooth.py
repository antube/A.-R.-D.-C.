import bluetooth

def write_blue(instructions):
	client_sock = None
	
	data = 'icommand,' + str(0) + ',' + str(1)+';'
	client_sock.send(data.encode())
	
	index = 0
	while index < len(instructions):
		serial_line = ""

		serial_line = client_sock.recv(9600)
		serial_line = serial_line.decode()

		if index == 0 or (serial_line[0] == "2" and serial_line[2] == "0"):
			data = 'icommand,' + str(instructions[index][0]) + ',' + str(instructions[index][0])+';'
			client_sock.send(data.encode())
			index += 1
		
		print (serial_line)

def blue_list_activation():
	pass

def bluetooth_connect(target_name, port):
	
	nearby_devices = bluetooth.discover_devices()

	for bdaddr in nearby_devices:
		if target_name == bluetooth.lookup_name( bdaddr ):
			target_address = bdaddr
			break

	if target_address is not None:
		print("found target bluetooth device with address", target_address)
	else:
		print("could not find target bluetooth device nearby")
		
	print("begining client connection setup")
	client_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	client_sock.connect((target_address, port))
	print("client connnection setup complete")