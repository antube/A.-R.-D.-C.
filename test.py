def Command_Test_Print(CMD, Arguments):
    counter = 1
    print ("Command: { " + CMD + " }")
    for argument in Arguments:
        print ("    Argument " + counter + ": { "+ argument + " }")
        counter += 1