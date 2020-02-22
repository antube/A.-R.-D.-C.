def help(Arguments):
    if len(Arguments) > 0:
        if Arguments[0].lower() == "add":
            print ("Takes two arguments")
            print ("Input")
            print (" ADD [/i or /e] [if /i add index] [direction] [time]")
        elif Arguments[0].lower() == "run":
            print ("Takes No Arguments")
            print ("Input:")
            print (" RUN")
        elif Arguments[0].lower() == "list":
            print ("Takes No Arguments")
            print ("Input")
            print (" LIST")
            print ("Output")
            print (" [Index] [Direction] [Time]")
        elif Arguments[0].lower() == "rm":
            print ("Takes one argument")
            print ("Input")
            print (" RM [index or /a]")
            print ("NOTE: The index is of an instruction is able to be attained through listing and copying the first number of the instruction")
        elif Arguments[0].lower() == "ch":
            print ("Takes three arguments")
            print ("Input")
            print (" CH [Index] [direction] [time]")
            print ("NOTE: It is a good idea to list the stored commmands before editing them\n type HELP LIST to show help for list")
    else:
        print ("RUN.........RUNs the robot over the USB")
        print ("ADD.........ADD a motion to the list")
        print ("LS..........LiSt all of the motions on the screen")
        print ("RM..........ReMove a paticular Command")
        print ("CH..........CHange a command in the list")
        print ("HELP........HELP shows this general list and also shows a more pointed help for each command")
        print ("WRITE.......WRITE the command list ot the Arduino")
        print ("BLCO........BLuetooth COnnect")