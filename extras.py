from serial import Serial
from os.path import exists

def arduino_list_write(instructions, Arguments):
    serial_line = ""
    index = 0

    if len(Arguments) > 0:
        print("Hello: Write Test")
        multiplier = 0
        command_length = int(instructions[index][1])
        command = int(instructions[index][0])
        print("command 1: " + hex(int(command)))
        
        command = command << 5
        
        if command_length >= 10 and command_length < 2551:
            commmand_length = command_length / 10
            multiplier = 1
            
        elif command_length >= 2550 and command_length < 25501:
            multiplier = 2
            command_length = command_length / 100
        
        print("command 2: " + hex(int(command)))
        command = command|int(multiplier)
        
        data1 = "icommand,6," + str(command) + ';'
        data2 = "icommand,7," + str(int(command_length)) + ';'
        
        print(data1)
        print(data2)
        print('Command: ' + hex(int(command)))
        print('Num: ' + hex(int(command_length)))
        print('Multiplier: ' + hex(multiplier))
        print('Length: ' + hex(int(instructions[index][1])))
    else:
        serUSB = Serial('/dev/ttyACM0')
        if exists('/dev/tty.usbserial'):
            serUSB = Serial('/dev/tty.usbserial')
        serial_line = serUSB.readline()
        serial_line.decode()
        while True or index >= len(instructions):
            if serial_line[0] == '2' and serial_line[2] == '5' or index == 0:
                print("Writing")
                multiplier = 0
                command_length = int(instructions[index][1])
                num = int(instructions[index][0])
                num << 13
                if command_length >= 40960 and command_length < 409600:
                    command_length /= 10
                elif command_length >= 409600 and command_length < 4096000:
                    multiplier = 8192
                    command_length /= 100
                multiplier << 8
                num = num|multiplier
                num = num|command_length
                data = "icommand,6," + str(num) + ';'
                print(data)
                serUSB.write(data.encode())
                index += 1
            elif serial_line[0] == '2' and serial_line[2] == '6' or index >= len(instructions):
                break
            serial_line = serUSB.read()
            serial_line.decode()