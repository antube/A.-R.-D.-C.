from serial import Serial
from os.path import exists

def write_usb(command_direction, command_time):
    #Arduino Uno
    if exists('/dev/ttyACM0'):
        serUSB = Serial('/dev/ttyACM0')
        serUSB.baudrate = 9600
        
        index = 0
        while index < len(command_direction):
            serial_line = ""
           #if index > 0:
            serial_line = serUSB.readline()
            serial_line = serial_line.decode()
            
            if serial_line[0] == "2" and serial_line[2] == "0" or index == 0:
                data = 'icommand,' + str(command_direction[index]) + ',' + str(command_time[index])+';'
                serUSB.write(data.encode())
                index += 1
            print (serial_line)
    #Arduino Mega
    elif exists('/dev/tty.usbserial'):
        serUSB = Serial('/dev/tty.usbserial')
        serUSB.baudrate = 9600
        
        index = 0
        while index < len(command_direction):
            serial_line = serUSB.readline()
            serial_line = serial_line.decode()

            if serial_line == "2,0; \n" or index == 0:
                data = 'icommand,' + str(command_direction[index]) + ',' + str(command_time[index])+';'
                serUSB.write(data.encode())
                index += 1
            print (serial_line)
    else:
        print ("Sorry No Arduino Connected")

def usb_list_activation():
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