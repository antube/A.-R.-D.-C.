def help(Arguments):
    if len(Arguments) > 0:
        print("\n### Argument Syntax ###")
        print("  Postion of arguments is important")
        print("    [] = argument")
        print("    | = or")
        print("    + = and")
        print("    ? = if previous argument is")
        print("    : = then include\n\n")
        if Arguments[0] == "add":
            print ("### ADD ###")
            print ("Takes 3 - 4 arguments")
            print ("  -i : insert at provided index")
            print ("  -e : append to end of list")
            print ("   i : index")
            print ("   d : direction")
            print ("        forward  : Move robot forward")
            print ("        backward : Move robot backward")
            print ("        left     : Turn robot left")
            print ("        right    : Turn robot right")
            print ("        stop     : Command robot to stop : Especially useful for lists stored on robot")
            print ("   t : time")
            print ("        Time is represented in milliseconds")
            print("")
            print ("Input")
            print ("  ADD [-i|-e] [?-i:i] [d+t]")
        elif Arguments[0] == "run":
            print ("### RUN ###")
            print ("Takes 2 or 4 Arguments")
            print ("    -u : Communicate with robot over usb")
            print ("    -b : Communicate with robot over bluetooth")
            print ("    -s : Run a single command specified in ")
            print ("    -d : Run the list stored in this program")
            print ("    -l : Run the list stored on robot")
            print ("     d : direction")
            print ("        forward  : Move robot forward")
            print ("        backward : Move robot backward")
            print ("        left     : Turn robot left")
            print ("        right    : Turn robot right")
            print ("        stop     : Command robot to stop : Especially useful for lists stored on robot")
            print ("     t : time")
            print ("        Time is represented in milliseconds")
            print ("")
            print ("Input:")
            print ("  RUN [-u|-b] [-s|-d|-l] [?-s:d+t]")
        elif Arguments[0] == "write":
            print ("### WRITE ###")
            print ("NOT IMPLEMENTED")
        elif Arguments[0].lower() == "ls":
            print ("Takes 0 Arguments")
            print ("Input")
            print ("  LS")
            print ("\nOutput")
            print ("  [Index] [Direction] [Time]")
        elif Arguments[0] == "rm":
            print ("Takes one argument")
            print ("    -a : CLEARS LIST : CAUTION")
            print ("     i : index       : Removes a command at a specified index")
            print("")
            print ("Input")
            print ("  RM [i|-a]")
            print ("NOTE: The index of a command is able to be attained using the LS command")
        elif Arguments[0] == "ch":
            print ("Takes 3 arguments")
            print ("Input")
            print ("  CH [i+d+t]")
            print ("NOTE: It is a good idea to LS the stored commmands before editing them")
    else:
        print ("### Implemented Commands ###")
        print ("RUN.........intitiates RUN of the robot")
        print ("ADD.........ADD a motion to the list")
        print ("LS..........LiSt all of the motions")
        print ("RM..........ReMove a paticular Command")
        print ("CH..........CHange a command in the list")
        print ("HELP........HELP shows this general list and also shows a more pointed help for each command")
        print ("BLCO........BLuetooth COnnect")
        print ("EXIT........EXIT program")
        print ("")
        print ("### Not Implemented Commands ###")
        print ("WRITE.......WRITE the command list ot the Arduino")