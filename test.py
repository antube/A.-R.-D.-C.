def command_test_print(CMD, Arguments):
    counter = 1
    print ("Command: { " + CMD + " }")
    for argument in Arguments:
        print ("    Argument " + str(counter) + ": { "+ argument + " }")
        counter += 1